import time
import sched

from stackunderflowed import fetch_configuration
from stackunderflowed.indexer import fetch_accounts_with_balance
from stackunderflowed.sender import send_grind_token

config = fetch_configuration()
s = sched.scheduler(time.time, time.sleep)


def _distribute_tokens(asset_id: int, time_till_next_distribution: int = 120):
    for address in fetch_accounts_with_balance(asset_id=33334727):
        send_grind_token(address, 1)

    s.enter(
        time_till_next_distribution,
        1,
        _distribute_tokens,
        kwargs={"asset_id": asset_id},
    )


def run_distributor():
    """Running work token distributor script that distributes daily rewards to HODLers"""
    print("Starting distributor")
    s.enter(0, 1, _distribute_tokens, kwargs={"asset_id": config.work_token_id})
    s.run()
