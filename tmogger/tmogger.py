#!/usr/bin/env python

import multiprocessing as mp
import sys
import re
import libtmux
import subprocess
import argparse

def _worker(name):
    pass

def _listener(name):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TBD")

    parser.add_argument("name", help="Name of the current task to be logged.")

    args = parser.parse_args()

    pool = mp.Pool(2)
    manager = mp.Manager()
    q = manager.Queue()
    listener = q
