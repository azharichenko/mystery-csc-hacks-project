from algosdk.v2client import indexer
import json
from pathlib import Path

cwd = Path.cwd()
config_file = cwd / "config.json"

with config_file.open() as f:
    config = json.load(f)


algod_address = "https://testnet-algorand.api.purestake.io/idx2"
headers = {
   "X-API-Key": config["api-key"],
}

indexer_client = indexer.IndexerClient("", algod_address, headers)

name = 'GRIND'
limit = 10
response = indexer_client.search_transactions(asset_id=33020017, limit=limit)

print("Asset search: " + json.dumps(response, indent=2, sort_keys=True))