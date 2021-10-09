"""
The supreme overlord script for everything this project i guess
"""
from argparse import ArgumentParser

from stackunderflowed.distributor import *
from stackunderflowed.indexer import *

if __name__ == "__main__":
    parser = ArgumentParser(description="")
    parser.add_argument("--distributor", action="store_true")

    args = parser.parse_args()

    if args.distributor:
        run_distributor()
