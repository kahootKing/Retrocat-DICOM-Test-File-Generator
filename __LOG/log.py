## log.py
#
# Modules in the /__LOG directory that defines functions pertaining to generating, writing, and deleting logs and their respective direrctories.

# -- (Log) Variables -- #
## logDir = "\log\
## logFilePrefix = 'log_'

import os
from datetime import datetime

# Logging Variables
# canLog = True
# -- (Log) Functions -- #

def create_log_dir():
    canLog = True
    logDir = os.getcwd() + "\\log\\"
    logDirExists = os.path.exists(logDir)
    if logDirExists:
        currentDate = get_date_time()[0]
        canLog = write_log_file(f"The logging directory for this program already exists: {logDir}", 4) 
    else:
        try:
            os.mkdir(logDir)
            canLog = write_log_file(logDir, f"The logging directory for this program did not exist and has been made: {logDir}", canLog, 4)
        except:
            print(f"The logging directory at {logDir} could not be created. Please check the file write permissions for the current Windows user.") ## replace with popup
            canLog = False
    return canLog


def write_log_file(logString, logType=1):
    from __main__ import canLog
    match logType:
        case 1:
            logPrefix = ""
        case 2:
            logPrefix = "|~INFO~| "
        case 3:
            logPrefix = "|~ERROR~| "
        case 4:
            logPrefix = "|~INITIALIZE~| "
        case 5:
            logPrefix = "|~SHUTDOWN~| "
        case 6:
            logPrefix = "|~DICOM~| "
        case 7:
            logPrefix = "|~HL7~| "
        case 8:
            logPrefix = "|USER ACTION~| "
        case _:
            logPrefix = "|~~| "

    if canLog:
        logDir = os.getcwd() + r"\log\\"
        todayLog, canLog = create_log_file()
        if canLog:
            logString = str(logString)
            currentTime = get_date_time()[1]
            try:
                with open (todayLog, 'a') as file:
                    file.write(currentTime + ": " + logPrefix + logString + "\n")
            except:
                print(f"The logging file at {todayLog} could not be written to. Please check the file write permissions for the current Windows user.") ## replace with popup
                canLog = False
    return canLog

    

def get_date_time():
    currentDate = datetime.today().strftime('%Y%m%d')
    currentTime = datetime.today().strftime('%H:%M:%S.%f')
    return currentDate, currentTime



def create_log_file():
    canLog = True
    logDir = os.getcwd() + r"\log\\"
    currentDate = get_date_time()[0]
    todayLog = logDir + 'log_' + currentDate + ".txt"
    todayLogExists = os.path.exists(todayLog)
    if todayLogExists == False:
        try:
            with open (todayLog, 'w') as file:
                pass
        except:
            print(f"The logging file at {todayLog} cannot be made. Please check the file write permissions for the current Windows user.") ## replace with popup
            canLog = False
    return todayLog, canLog