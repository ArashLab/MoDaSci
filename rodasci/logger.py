### To access version
import importlib.resources
from pathlib import Path

packageName='rodasci'
moduleName='logger'
with importlib.resources.path(packageName, 'VERSION') as path:
    print(path)
    moduleVersion = Path(path).read_text()

if __name__ == '__main__':
    print(f'This is `{packageName}.{moduleName}` version `{moduleVersion}`')
    print('This module is not executable.')
    exit(0)
    
import sys
import logging
from datetime import datetime
import random
import string

from .util import GetCaller, AddLogDetails

class Logger:

    initialised = None ### each interface function musch check if the class is initialised befor making actions
    loggerName = None
    externalReformMessage = None
    defaultLogLevel = None
    logFilePath = None
    logFileHandler = None
    logger = None

    @classmethod
    def Init(cls,
        logFilePrefix='AbLogger', 
        logFilePath=None,
        logLevel=logging.DEBUG,
        logFormat='%(asctime)s\t%(levelname)s\t%(message)s',
        externalReformMessage=AddLogDetails,
        defaultLogLevel='INFO',
        loggerName='AbLogger'):

        cls.loggerName = loggerName
        cls.externalReformMessage = externalReformMessage
        cls.defaultLogLevel = defaultLogLevel
        
        ### Create the ogger instance
        cls.logger = logging.getLogger(loggerName)
        

        if logFilePath:
            cls.logFilePath = logFilePath
        else:
            randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            now = str(datetime.now().strftime("%Y%m%d-%H%M%S"))
            cls.logFilePath = f'{logFilePrefix}.{now}.{randomString}.log.tsv'
        
        ### Exception if file does not exist        

        cls.logger.setLevel(logLevel)
        cls.logFileHandler = logging.FileHandler(filename=cls.logFilePath,  mode='w')
        formatter = logging.Formatter(logFormat)
        cls.logFileHandler.setFormatter(formatter)
        cls.logger.addHandler(cls.logFileHandler)

        print(f'*** logger is initialised to write to {cls.logFilePath}')

    @classmethod
    def __ReformMessage(cls, message, caller):
        message = cls.externalReformMessage(message, caller)
        return message

    @classmethod
    def LogException(cls, message='An exception occurred.', caller=None):
        if not caller:
            caller = GetCaller()
        message = cls.__ReformMessage(message, caller)

        cls.logger.exception(message)

    @classmethod
    def LogExit(cls, message='An error occurred.', caller=None):
        if not caller:
            caller = GetCaller()
        
        message = cls.__ReformMessage(message, caller)

        cls.logger.error(message)
        print(message, file=sys.stderr)
        exit(1)

    @classmethod
    def CheckValue(cls, value, validValues, caller=None):
        if not caller:
            caller = GetCaller()

        if value not in validValues:
            cls.LogExit(f'The value: `{value}` is not in the valid values list: `{validValues}`', caller=caller)

    @classmethod
    def CheckTypeExact(cls, value, validTypes, caller=None):
        if not caller:
            caller = GetCaller()

        if type(value) not in validTypes:
            cls.LogExit(f'The given value: `{value}` is of type `{type(value)}` that is not in the valid type list: `{validTypes}`', caller=caller)

    @classmethod
    def CheckType(cls, value, validTypes, caller=None):
        if not caller:
            caller = GetCaller()

        if not any([isinstance(value, validType) for validType in validTypes]):
            cls.LogExit(f'The given value: `{value}` is of type `{type(value)}` that does not match any of types in the valid type list: `{validTypes}`', caller=caller)
    
        
    @classmethod
    def __LogOptionalPrint(cls, message, level, fileToPrint, doPrint, caller):
        if not caller:
            caller = GetCaller()
        message = cls.__ReformMessage(message, caller)

        cls.CheckValue(level, ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'])

        if not doPrint and fileToPrint:
            cls.LogException('Why you set the fileToPrint when doPrint is False')

        if doPrint and not fileToPrint:
            if level in ['CRITICAL', 'ERROR']:
                fileToPrint = sys.stderr
            else:
                fileToPrint = sys.stdout

        if doPrint:
            print(message, file=fileToPrint)

        cls.logger.log(getattr(logging, level),  message)

    @classmethod
    def Log(cls, message='Log Message', level=None, caller=None):
        if not caller:
            caller = GetCaller()
        if not level:
            level = cls.defaultLogLevel
        cls.__LogOptionalPrint(message, level=None, fileToPrint=None, doPrint=False, caller=caller)


    @classmethod
    def LogPrint(cls, message='Log Message', level=None, fileToPrint=None, caller=None):
        if not caller:
            caller = GetCaller()
        if not level:
            level = cls.defaultLogLevel
        cls.__LogOptionalPrint(message, level, fileToPrint, doPrint=True, caller=caller)