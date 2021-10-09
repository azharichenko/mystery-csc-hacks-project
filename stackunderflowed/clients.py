from typing import Dict, Optional

from algosdk.v2client import indexer
from algosdk.v2client import algod

from stackunderflowed import fetch_configuration, ProjectConfiguration

ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
INDEXER_ADDRESS = "https://testnet-algorand.api.purestake.io/idx2"


algod_client: Optional[algod.AlgodClient] = None
indexer_client: Optional[indexer.IndexerClient] = None
config: ProjectConfiguration = fetch_configuration()


def _get_header() -> Dict:
    return {"X-API-Key": config.api_key}


def fetch_indexer_client() -> indexer.IndexerClient:
    global indexer_client
    if indexer_client is None:
        indexer_client = indexer.IndexerClient(
            config.api_key, INDEXER_ADDRESS, _get_header()
        )
    return indexer_client


def fetch_algod_client() -> algod.AlgodClient:
    global algod_client
    if algod_client is None:
        algod_client = algod.AlgodClient(
            config.api_key, ALGOD_ADDRESS, headers=_get_header()
        )
    return algod_client
