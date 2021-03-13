import logging
import logging.config
import platform
import configparser

logging.config.fileConfig('conf/logging.conf', defaults={'logfilename':'logs/example6.log'})

# create logger
logger = logging.getLogger('root')

def myFunc():
    print("this is func")
    logger.debug("info inside func")
    logger.info("debug inside func")
    logger.warning("warn inside func")
    logger.error("error inside func")
    logger.critical("critical inside func")

print(logger.__getattribute__("name"))
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
logger.critical('hostname test'+platform.machine()+platform.system())

myFunc()

