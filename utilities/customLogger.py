import logging
import datetime
class Log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\easemytrip.log",format='%(asctime)s:%(levelname)s:%(massage)s',datefmt="%Y-%m-%d %H:%M",force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger