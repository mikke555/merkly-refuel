from data.const import MERKLY_CONTRACTS, LAYERZERO_CHAINS_ID, ABI_MERKLY_REFUEL, CHAIN_DATA as DATA
from config import SLEEP_FROM, SLEEP_TO, SHUFFLE_WALLETS, FROM_CHAIN, TO_CHAIN, MIN_AMOUNT, MAX_AMOUNT
from helpers import get_web3, sign_tx, add_gas_limit_layerzero, check_status_tx, intToDecimal, sleeping, cheker_gwei, generate_refuel_params

from loguru import logger
from eth_abi import encode
from web3 import Web3

from sys import stderr
import random


logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <3}</level> | <level>{message}</level>")


def get_adapterParams(gaslimit: int, amount: int):
    return Web3.to_hex(encode(["uint16", "uint64", "uint256"], [2, gaslimit, amount])[30:])


def merkly_refuel(from_chain, to_chain, amount, private_key):
    global module_str

    try:
        web3 = get_web3(from_chain)
        account = web3.eth.account.from_key(private_key)
        wallet = account.address
        nonce = web3.eth.get_transaction_count(wallet)
        
        module_str = f'merkly_refuel : {from_chain} => {to_chain}'
        logger.info(module_str)

        contract = web3.eth.contract(address=Web3.to_checksum_address(
            MERKLY_CONTRACTS[from_chain]), abi=ABI_MERKLY_REFUEL)

        value = intToDecimal(amount, 18)
        adapterParams = get_adapterParams(250000, value) + wallet[2:].lower()
        
        
        send_value = contract.functions.estimateGasBridgeFee(
            LAYERZERO_CHAINS_ID[to_chain], False, adapterParams).call()
        
        tx_params = { "from": wallet, "value": send_value[0], "nonce": nonce }
        
        if FROM_CHAIN == 'zksync': tx_params['gasPrice'] = web3.eth.gas_price
        elif FROM_CHAIN == 'bsc': tx_params['gasPrice'] = 10000000000 

        contract_txn = contract.functions.bridgeGas(
            LAYERZERO_CHAINS_ID[to_chain],
            '0x0000000000000000000000000000000000000000',  # _zroPaymentAddress
            adapterParams
        ).build_transaction(tx_params)
        
           
        if amount > 0:
            contract_txn = add_gas_limit_layerzero(web3, contract_txn)

            tx_hash = sign_tx(web3, contract_txn, private_key)
            tx_link = f'{DATA[from_chain]["scan"]}/{tx_hash}'

            status = check_status_tx(from_chain, tx_hash)
            
            if status == 1:
                logger.success(f'{module_str} | {tx_link}')
                return "success"

        else:
            logger.error(f"{module_str} : no balance")

    except Exception as error:
        logger.error(f'{module_str} | {error}')


if __name__ == '__main__':
    with open("keys.txt", "r") as file:
        keys = [line.strip() for line in file.readlines()]

        if SHUFFLE_WALLETS:
            random.shuffle(keys)
            
        while keys:
            cheker_gwei()
            
            key = keys.pop(0)
            to, amount = generate_refuel_params(FROM_CHAIN, TO_CHAIN, MIN_AMOUNT, MAX_AMOUNT)
                
            success = merkly_refuel(FROM_CHAIN, to, amount, key)
            
            if keys and success:
                sleeping(SLEEP_FROM, SLEEP_TO)
            
    print("\nExecution finished\n")