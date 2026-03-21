## dicomReadWrite.py

from pydicom import dcmread, dcmwrite

## Var
dcmFile = ""

def read_files(filePath):
    dcmFile = dcmread(filePath)