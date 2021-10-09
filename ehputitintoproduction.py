"""
The supreme overlord script for everything this project i guess
"""
import sched
from argparse import ArgumentParser

import stackunderflowed


def run_distributor():
    """Running work token distributor script that distributes daily rewards to HODLers"""
    pass


if __name__ == "__main__":
    parser = ArgumentParser(description="")
    parser.add_argument("--distributor", action="store_true")

    args = parser.parse_args()

    if args.distributor:
        run_distributor()
