import logging
from modules.setup import setup


setup()
logger = logging.getLogger('infoLogger')
logger.info('info message')