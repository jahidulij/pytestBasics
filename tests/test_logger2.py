import logging

logging.basicConfig(filename="C:/Users/JahidulIslam/PycharmProjects/pytestTutorialPoints/logs/test.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
