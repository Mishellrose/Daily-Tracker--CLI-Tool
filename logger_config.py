

import logging
import os

def setup_logger():
    logger = logging.getLogger("todo_app")
    logger.setLevel(logging.DEBUG)

    # Get current directory (important!)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(BASE_DIR, "app.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # File handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger