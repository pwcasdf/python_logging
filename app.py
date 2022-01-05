import datetime, time
from flask import Flask
import logging
import sys

app = Flask(__name__)

# set defualt logger level
# logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# logger object creation and set logging level, debug >> info >> warning >> error >> critical
testLogger = logging.getLogger('not_default')
streamHandler = logging.StreamHandler(sys.stdout)
testLogger.addHandler(streamHandler)
testLogger.setLevel(logging.INFO)

testLogger2 = logging.getLogger('not_default2')
streamHandler2 = logging.StreamHandler(sys.stderr)
testLogger2.addHandler(streamHandler2)
testLogger2.setLevel(logging.INFO)


@app.route('/')
def hello_world():
    print('\n\n--------------------------------------------------------------\n\n')
    print(datetime.datetime.now(), 'print')
    
    app.logger.info('info app.logger')
    
    logging.debug('debug default')
    logging.info('info default')
    logging.warning('warning default')

    testLogger.debug('debug testLogger')
    testLogger.info('info testLogger')
    testLogger.warning('warning testLogger')

    testLogger2.debug('debug testLogger2')
    testLogger2.info('info testLogger2')
    testLogger2.warning('warning testLogger2')
    
    return str(datetime.datetime.now())