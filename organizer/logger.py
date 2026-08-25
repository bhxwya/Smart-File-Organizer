import logging

logging.basicConfig(
    filename= "logs/log.log",
    level= logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
