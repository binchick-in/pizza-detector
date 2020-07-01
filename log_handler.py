import logging

log_format_str = (
    "[%(asctime)s]:[%(levelname)s]:[%(filename)s %(lineno)d]:[%(funcName)s]:%(message)s"
)
logging.basicConfig(format=log_format_str, level=logging.INFO)


def get_logger(name: str):
    return logging.getLogger(name)
