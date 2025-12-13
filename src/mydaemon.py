#!/usr/bin/env python3
import time
import logging
from daemon import DaemonContext
import os

# Ambil direktori file mydaemon.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path ke folder logs
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
LOG_FILE = os.path.join(LOG_DIR, "mydaemon.log")

# Pastikan folder logs ada
os.makedirs(LOG_DIR, exist_ok=True)

def run():
    logging.info("Daemon started")
    while True:
        logging.info("Daemon berjalan... monitoring sistem.")
        time.sleep(10)

if __name__ == "__main__":
    with DaemonContext(
        working_directory="/",
        umask=0o022
    ):
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format="[%(asctime)s] %(message)s"
        )
        run()
