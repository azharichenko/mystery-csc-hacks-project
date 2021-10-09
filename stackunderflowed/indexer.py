import json
from typing import Dict, List

from stackunderflowed import indexer_client


def _fetch_recent_transactions(asset_id: int, limit: int = 10) -> List[Dict]:
    response = indexer_client.search_transactions(asset_id=asset_id, limit=limit)
    # json.dumps(, indent=2, sort_keys=True)
    return response


def fetch_recent_grind_transactions() -> List[Dict]:
    return _fetch_recent_transactions(asset_id=33020017)
