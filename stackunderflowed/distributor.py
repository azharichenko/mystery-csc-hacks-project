import sched

from stackunderflowed import fetch_configuration
from stackunderflowed.models import Participant
from stackunderflowed.sender import send_grind_token

config = fetch_configuration()
s = sched.scheduler()


def _distribute_tokens(asset_id: int, time_till_next_distribution: int = 100):
    send_grind_token("", 1)
    s.enter(0, 1, _distribute_tokens, kwargs={"asset_id": asset_id})


def run_distributor():
    """Running work token distributor script that distributes daily rewards to HODLers"""

    s.enter(0, 1, _distribute_tokens, kwargs={"asset_id": config.work_token_id})
    s.run()
