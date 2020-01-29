import logging.handlers

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
file_handler = logging.handlers.TimedRotatingFileHandler('./log/root.log', 'D', 1, 7)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(filename)s:%(lineno)s - %(funcName)s() - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(file_handler)
