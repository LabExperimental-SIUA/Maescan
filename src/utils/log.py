import logging
import os.path
homedir = os.path.expanduser('~')

#create logging types
#log into file
logging.basicConfig(filename=homedir + '/.librescan/librescan.log',format = '%(asctime) - s %(levelname)s:%(message)s',level=logging.DEBUG)

#logger types
#logging.debug('debug message')
#logging.info('info message')
#logging.warn('warn message')
#logging.error('error message')
#logging.critical('critical message')	

