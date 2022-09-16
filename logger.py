import logging
import sys


def setup_logger(name=__name__):
    # Create a custom logger
    logger = logging.getLogger(name=__name__)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler("./logs.log")

    # Add formatters
    format_ = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    c_format = logging.Formatter(format_)
    f_format = logging.Formatter(format_)
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


if __name__ == "__main__":
    setup_logger(__name__)
