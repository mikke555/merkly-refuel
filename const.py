import json

with open(f"data/erc20.json", "r") as file:
    ERC20_ABI = json.load(file)

LAYERZERO_CHAINS_ID = {
    'kava'      : 177,
    'linea'     : 183,
    'base'      : 184,
    'zora'      :195,
    'scroll'    : 214,
    'conflux'    : 212,
    'celo'      : 125,
}

MERKLY_CONTRACTS = {
    'optimism'      : '0xa2c203d7ef78ed80810da8404090f926d67cd892',
    'bsc'           : '0xfdc9018af0e37abf89233554c937eb5068127080',
    'arbitrum'      : '0xaa58e77238f0e4a565343a89a79b4addd744d649',
    'polygon'       : '0xa184998ec58dc1da77a1f9f1e361541257a50cf4',
    'celo'          : '0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0',
}





