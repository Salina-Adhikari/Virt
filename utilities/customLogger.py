import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "Logs")
        os.makedirs(log_dir, exist_ok=True)

        log_path = os.path.join(log_dir, "automation.log")

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            filename=log_path,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )
        logger = logging.getLogger("automationLogger")
        logger.info("Logger initialized and writing to automation.log.")

        return logger
