import json
from settings import *


def dict_to_bytes(data):
    return json.dumps(data, sort_keys=SORT_KEYS, ensure_ascii=ENSURE_ASCII, indent=INDENT).encode(ENCODING)


def bytes_to_dict(data):
    return json.loads(data(BUF_SIZE).decode(ENCODING))
