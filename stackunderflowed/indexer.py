import json
from typing import Any, Dict, Generator, List, Optional

from stackunderflowed.clients import fetch_indexer_client


IGNORE_ADDRESS = [
    "MEK6YSJUCQVR47XFRKO3HCLUM67WB6ZAWYVNQGVSFYQD5V4DLHRT2ZRURQ",
]


def fetch_accounts_with_balance(
    asset_id: int, min: int = 1
) -> Generator[str, None, None]:
    client = fetch_indexer_client()
    response: Dict[str, Any] = {"next-token": None, "balances": []}
    next_page = None

    while "next-token" in response:
        response = client.asset_balances(
            asset_id=asset_id,
            min_balance=0,
            next_page=response["next-token"],
        )

        for balance in response["balances"]:
            if balance["address"] not in IGNORE_ADDRESS:
                yield balance["address"]
