#!/usr/bin/env python3
import time
import logging
from daemon import DaemonContext
import os
import logging

log_path = os.path.join(os.path.expanduser("~"), "mydaemon.log")


# Konfigurasi logging
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="[%(asctime)s] %(message)s"
)

def run():
    while True:
        logging.info("Daemon berjalan... monitoring sistem.")
        time.sleep(10)

if __name__ == "__main__":
    with DaemonContext():
        run()
