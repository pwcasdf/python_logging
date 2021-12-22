import datetime, time
from flask import Flask
import logging
import sys

app = Flask(__name__)

# set defualt logger level
#logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# logger object creation and set logging level, debug >> info >> warning >> error >> critical
testLogger = logging.getLogger('not_default')
#streamHandler = logging.StreamHandler(sys.stdout)
#testLogger.addHandler(streamHandler)
testLogger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    print(datetime.datetime.now(), 'this is print@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    app.logger.info('this is app.logger.info^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    logging.info('this is info!!!!!!!!!!!!!!!!!!!!!!!!!!')
    logging.warning('this is warning#################################')
    logging.debug('this is debug1231231231')

    testLogger.info('this is info testLogger!!!!!!!!!!!!!!!!!!!!!!!!!!')
    testLogger.warning('this is warning testLogger#################################')
    testLogger.debug('this is debug testlogger 123413414212414142124')
    return str(datetime.datetime.now())