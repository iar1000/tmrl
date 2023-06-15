#!/usr/bin/env python3

import os
import sys
import logging


LOG_FORMAT = "%(name)-35s - %(levelname)-8s - %(message)s"

def setup_logger(logger, name, level=logging.DEBUG, fmt=None):
        for handler in logger.handlers:
            logger.removeHandler(handler)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter("%(name)-20s - %(levelname)-8s - %(message)s")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.setLevel(level)
