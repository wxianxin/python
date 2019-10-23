import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
logging.debug("This message should appear on the console")

# Displaying date/time
import logging

logging.basicConfig(format="%(asctime)s %(message)s")
logging.warning("is when this event was logged.")

# loggger
import logging

logger = logging.getLogger("my_app")
file_handler = logging.FileHandler("my_app.log")
stream_handler = logging.StreamHandler()
formatter = logging.Formatter(
    fmt="%(asctime)s %(levelname)s: %(message)s", datefmt="%s"
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
logger.warning("yoyoyo")
