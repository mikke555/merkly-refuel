from data.const import CHAIN_DATA as DATA
from config import MAX_GWEI

from web3.middleware import geth_poa_middleware
from web3 import Web3
from loguru import logger
from tqdm import tqdm

import random
import time
import json
import csv


max_time_check_tx_status = 360
w3_eth = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))


def sign_tx(web3, contract_txn, privatkey):
    signed_tx = web3.eth.account.sign_transaction(contract_txn, privatkey)
    raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = web3.to_hex(raw_tx_hash)

    return tx_hash


def cheker_gwei():
    max_gwei = MAX_GWEI * 10 ** 9
    if w3_eth.eth.gas_price > max_gwei:
        logger.info('Gas is too high, falling asleep')
        while w3_eth.eth.gas_price > max_gwei:
            time.sleep(60)
        logger.info('Gas is back to normal, continue')


def check_status_tx(chain, tx_hash):
    start_time_stamp = int(time.time())

    while True:
        try:
            rpc_chain = DATA[chain]['rpc']
            web3 = Web3(Web3.HTTPProvider(rpc_chain))
            status_ = web3.eth.get_transaction_receipt(tx_hash)
            status = status_["status"]

            if status in [0, 1]:
                return status

        except:
            time_stamp = int(time.time())
            if time_stamp - start_time_stamp > max_time_check_tx_status:
                logger.info(f'не получили tx_status за {max_time_check_tx_status} sec, думаем что tx is success')
                return 1
            time.sleep(1)


def add_gas_limit(web3, contract_txn):
    value = contract_txn['value']
    contract_txn['value'] = 0
    pluser = [1.02, 1.05]
    gasLimit = web3.eth.estimate_gas(contract_txn)
    contract_txn['gas'] = int(gasLimit * random.uniform(pluser[0], pluser[1]))

    contract_txn['value'] = value
    return contract_txn


def add_gas_limit_layerzero(web3, contract_txn):
    pluser = [1.05, 1.07]
    gasLimit = web3.eth.estimate_gas(contract_txn)
    contract_txn['gas'] = int(gasLimit * random.uniform(pluser[0], pluser[1]))
    return contract_txn


def get_web3(chain):
    rpc = DATA[chain]['rpc']
    web3 = Web3(Web3.HTTPProvider(rpc))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return web3


def intToDecimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"] * decimal)))


def sleep(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)
        
def sleep_silently(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    time.sleep(x)
        
    
def generate_refuel_params(FROM_CHAIN, TO_CHAIN, MIN_AMOUNT, MAX_AMOUNT):
    if TO_CHAIN: 
        to_chain = TO_CHAIN
        rand_amount = round(random.uniform(MIN_AMOUNT, MAX_AMOUNT), 8)
    else:
        with open('data/routes.json') as f:
            routes = json.load(f)
            
        from_chain = routes[FROM_CHAIN]
        
        rand_dest = random.choice(from_chain)
        to_chain = list(rand_dest.keys())[0]

        min_val = rand_dest[to_chain]['min']
        max_val = rand_dest[to_chain]['max']
        rand_amount = round(random.uniform(min_val, max_val), 8)

    return to_chain, rand_amount


def write_to_csv(address, key, result):
    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(['address', 'key', 'result'])

        writer.writerow([address, key,  result])




