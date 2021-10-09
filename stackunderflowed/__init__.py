import json
from pathlib import Path

from algosdk.v2client import algod
from algosdk import mnemonic

cwd = Path.cwd()
config_file = cwd / "config.json"

with config_file.open() as f:
    config = json.load(f)

# Setup HTTP client w/guest key provided by PureStake
algod_token = config["api-key"]
ALGOD_ADDRESS = 'https://testnet-algorand.api.purestake.io/ps2'
purestake_token = {'X-Api-key': algod_token}

# Initalize throw-away account for this example - check that is has funds before running script
mnemonic_phrase = config["wallet"]
account_private_key = mnemonic.to_private_key(mnemonic_phrase)
account_public_key = mnemonic.to_public_key(mnemonic_phrase)

# One client to rule them all
algodclient = algod.AlgodClient(algod_token, algod_address, headers=purestake_token)
