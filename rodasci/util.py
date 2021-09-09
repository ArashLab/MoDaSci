### To access version
import importlib.resources
from pathlib import Path

packageName='rodasci'
moduleName='util'
with importlib.resources.path(packageName, 'VERSION') as path:
    print(path)
    moduleVersion = Path(path).read_text()

if __name__ == '__main__':
    print(f'This is `{packageName}.{moduleName}` version `{moduleVersion}`')
    print('This module is not executable.')
    exit(0)

### To access caller information
from inspect import getframeinfo, stack
    

def GetCaller(level=2):
    ### level=1 is the caller of GetCaller
    ### level=2 is the caller of the fuction that calls GetCaller
    return getframeinfo(stack()[level][0])

### This is an example function to pass to the ReformMessage
def AddLogDetails(message, caller):
    if not isinstance(caller, dict):
        caller = dict()
    functionName = caller.get('function', 'None')
    fileName = caller.get('filename', 'None')
    lineNum = caller.get('lineno', 'None')
    message = f'{functionName}\t{message}\t{fileName}\t{lineNum}'
    return message