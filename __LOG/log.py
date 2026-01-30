## log.py
#
# Modules in the /__LOG directory that defines functions pertaining to generating, writing, and deleting logs and their respective direrctories.

# -- (Log) Variables -- #
## logDir = "\log\
## logFilePrefix = 'log_'

import os
from datetime import datetime


# -- (Log) Functions -- #

def create_log_dir(rootPath):
    currentDate = get_date_time()[0]
    logDir = rootPath + r"\log\\"
    newLogDir = os.path.exists(logDir)
    if newLogDir:
        write_log_file(logDir, f"The logging directory for this program already exists: {logDir}", 3) 
    else:
        try:
            os.mkdir(logDir)
            write_log_file(logDir, f"The logging directory for this program did not exist and has been made: {logDir}", 3)
        except:
            print(f"The logging directory at {logDir} could not be created. Please check the file write permissions for the current Windows user.")
    return logDir


def write_log_file(logDir, logString, logType=1):
    
    match logType:
        case 1:
            logPrefix = "|~INFO~| "
        case 2:
            logPrefix = "|~ERROR~| "
        case 3:
            logPrefix = "|~INITIALIZE~| "
        case 4:
            logPrefix = "|~SHUTDOWN~| "
        case 5:
            logPrefix = "|~DICOM~| "
        case 6:
            logPrefix = "|~HL7~| "
        case 7:
            logPrefix = ""
        case _:
            logPrefix = "|~~| "

    todayLog = create_log_file(logDir)
    logString = str(logString)
    currentTime = get_date_time()[1]
    try:
        with open (todayLog, 'a') as file:
            file.write(currentTime + ": " + logPrefix + logString + "\n")
    except:
        print(f"The logging file at {todayLog} could not be written to. Please check the file write permissions for the current Windows user.")

    

def get_date_time():
    currentDate = datetime.today().strftime('%Y%m%d')
    currentTime = datetime.today().strftime('%H:%M:%S.%f')
    return currentDate, currentTime



def create_log_file(logDir):
    currentDate = get_date_time()[0]
    todayLog = logDir + 'log_' + currentDate + ".txt"
    todayLogExists = os.path.exists(todayLog)
    if todayLogExists == False:
        try:
            with open (todayLog, 'w') as file:
                pass
        except:
            print(f"The logging file at {todayLog} cannot be made. Please check the file write permissions for the current Window's user.")
    return todayLog