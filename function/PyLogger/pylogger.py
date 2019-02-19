import logging
from time import strftime

filename = "log/{}-{}.log".format("RPG_FOP", strftime("%Y_%m_%d_%H_%M_%S"))

pylogger = logging.getLogger(__name__)
pylogger.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename, 'w', 'utf-8')
formatter = logging.Formatter(
    fmt='[%(asctime)s][%(levelname)s] : [%(filename)s][%(funcName)s] : %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

handler.setFormatter(formatter)
pylogger.addHandler(handler)
