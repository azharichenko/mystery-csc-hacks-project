import json
from pathlib import Path
from typing import Optional

from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk.v2client import indexer

# Data directory and configuration file stuff
from stackunderflowed.state import load_current_project_state, fetch_configuration


ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
INDEXER_ADDRESS = "https://testnet-algorand.api.purestake.io/idx2"


checked = load_current_project_state()

if not checked:
    exit()


config = fetch_configuration()

# Setup HTTP client w/guest key provided by PureStake
algod_token = config.api_key
purestake_token = {"X-Api-key": algod_token}
headers = {
    "X-API-Key": algod_token,
}

# Initalize throw-away account for this example - check that is has funds before running script
mnemonic_phrase = config.custodian_wallet_mnemonic
account_private_key = mnemonic.to_private_key(mnemonic_phrase)
account_public_key = mnemonic.to_public_key(mnemonic_phrase)

# One client to rule them all
indexer_client = indexer.IndexerClient("", INDEXER_ADDRESS, headers)
algod_client = algod.AlgodClient(algod_token, ALGOD_ADDRESS, headers=purestake_token)
