import logging
import logging.config
from logging.config import dictConfig
import yaml


with open('config/logging.yml', 'r') as stream:
    logging_config = yaml.load(stream)

dictConfig(logging_config)