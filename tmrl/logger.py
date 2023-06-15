#!/usr/bin/env python3

import os
import sys
import logging


initialized_loggers = dict()

def setup_logger(logger, name, level=logging.DEBUG, fmt=None):
        if name in initialized_loggers.keys():
            return
        for handler in logger.handlers:
            logger.removeHandler(handler)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter("%(name)-20s - %(levelname)-8s - %(message)s")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.info("setup logger")
        initialized_loggers[name] = True