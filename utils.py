import json
import logging
from logging.handlers import RotatingFileHandler
from settings import *


def dict_to_bytes(data):
    return json.dumps(data, sort_keys=SORT_KEYS, ensure_ascii=ENSURE_ASCII, indent=INDENT).encode(ENCODING)


def bytes_to_dict(data):
    return json.loads(data(BUF_SIZE).decode(ENCODING))

def start_serverlog(path):
    logging.basicConfig(
        filename='server.log',
        format='%(levelname)-10s %(asctime)s %(message)s',
        level=logging.DEBUG
    )
    log = logging.getLogger('basic')
    log.debug('start log')
    handler = RotatingFileHandler(path, maxBytes=20)
    log.addHandler(handler)

    return log



def start_log(logname):
    logging.basicConfig(
        filename=logname + '.log',
        format='%(levelname)-10s %(asctime)s %(message)s',
        level=logging.DEBUG
    )
    log = logging.getLogger('basic')
    log.debug('start log')
    return log

def log_debug(log,msg):
    return log.debug(msg)

def log_info(log,msg):
    return log.info(msg)

def log_warning(log,msg):
    return log.warning(msg)

def log_critical(log,msg):
    return log.critical(msg)

