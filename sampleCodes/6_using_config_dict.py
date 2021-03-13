import logging
import logging.config

logging.config.fileConfig('conf/logging.conf', defaults={'logfilename': 'logs/myspeciallogfile.log'})

# create logger
logger = logging.getLogger('root')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')