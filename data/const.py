import json


with open(f"data/merkly.json", "r") as file:
    ABI_MERKLY_REFUEL = json.load(file)
    
LAYERZERO_CHAINS_ID = {
    'kava'      : 177,
    'linea'     : 183,
    'base'      : 184,
    'zora'      : 195,
    'scroll'    : 214,
    'conflux'   : 212,
    'celo'      : 125,
    'zksync'    : 165,
    'nova'      : 175,
    'astar'     : 210,
    'opbnb'     : 202,
    'gnosis'    : 145,
    'klaytn'    : 150,
    'beam'      : 198,
    'moonbeam'  : 126,
    'harmony'   : 116,
}

MERKLY_CONTRACTS = {
    'optimism'      : '0xa2c203d7ef78ed80810da8404090f926d67cd892',
    'bsc'           : '0xfdc9018af0e37abf89233554c937eb5068127080',
    'arbitrum'      : '0xaa58e77238f0e4a565343a89a79b4addd744d649',
    'polygon'       : '0xa184998ec58dc1da77a1f9f1e361541257a50cf4',
    'celo'          : '0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0',
    'zksync'        : '0x6dd28C2c5B91DD63b4d4E78EcAC7139878371768',
    'base'          : '0xF882c982a95F4D3e8187eFE12713835406d11840'
}

CHAIN_DATA = {
    'optimism'      : { 'rpc': 'https://rpc.ankr.com/optimism', 'scan': 'https://optimistic.etherscan.io/tx', 'token': 'ETH', 'chain_id': 10 },
    'ethereum'      : { 'rpc': 'https://rpc.ankr.com/eth', 'scan': 'https://etherscan.io/tx', 'token': 'ETH', 'chain_id': 1 },
    'bsc'           : { 'rpc': 'https://rpc.ankr.com/bsc', 'scan': 'https://bscscan.com/tx', 'token': 'BNB', 'chain_id': 56 },
    'polygon'       : { 'rpc': 'https://rpc.ankr.com/polygon', 'scan': 'https://polygonscan.com/tx', 'token': 'MATIC', 'chain_id': 137 },
    'polygon_zkevm' : { 'rpc': 'https://zkevm-rpc.com', 'scan': 'https://zkevm.polygonscan.com/tx', 'token': 'ETH', 'chain_id': 1101 },
    'arbitrum'      : { 'rpc': 'https://rpc.ankr.com/arbitrum', 'scan': 'https://arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42161 },
    'nova'          : { 'rpc': 'https://nova.arbitrum.io/rpc', 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42170 },
    'avalanche'     : { 'rpc': 'https://rpc.ankr.com/avalanche', 'scan': 'https://snowtrace.io/tx', 'token': 'AVAX', 'chain_id': 43114 },
    'fantom'        : { 'rpc': 'https://rpc.ankr.com/fantom', 'scan': 'https://ftmscan.com/tx', 'token': 'FTM', 'chain_id': 250 },
    'nova'          : { 'rpc': 'https://nova.arbitrum.io/rpc', 'scan': 'https://nova.arbiscan.io/tx', 'token': 'ETH', 'chain_id': 42170},
    'zksync'        : { 'rpc': 'https://mainnet.era.zksync.io', 'scan': 'https://explorer.zksync.io/tx', 'token': 'ETH', 'chain_id': 324 },
    'celo'          : { 'rpc': 'https://1rpc.io/celo', 'scan': 'https://celoscan.io/tx', 'token': 'CELO', 'chain_id': 42220 },
    'gnosis'        : { 'rpc': 'https://rpc.ankr.com/gnosis', 'scan': 'https://gnosisscan.io/tx', 'token': 'xDAI', 'chain_id': 100 },
    'core'          : { 'rpc': 'https://rpc.coredao.org', 'scan': 'https://scan.coredao.org/tx', 'token': 'CORE', 'chain_id': 1116},
    'harmony'       : { 'rpc': 'https://api.harmony.one', 'scan': 'https://explorer.harmony.one/tx', 'token': 'ONE', 'chain_id': 1666600000 },
    'moonbeam'      : { 'rpc': 'https://rpc.ankr.com/moonbeam', 'scan': 'https://moonscan.io/tx', 'token': 'GLMR', 'chain_id': 1284 },
    'moonriver'     : { 'rpc': 'https://moonriver.public.blastapi.io', 'scan': 'https://moonriver.moonscan.io/tx', 'token': 'MOVR', 'chain_id': 1285 },
    'linea'         : { 'rpc': 'https://rpc.linea.build', 'scan': 'https://lineascan.build/tx', 'token': 'ETH', 'chain_id': 59144 },
    'base'          : { 'rpc': 'https://base.llamarpc.com', 'scan': 'https://basescan.org/tx', 'token': 'ETH', 'chain_id': 8453 },
}
    
