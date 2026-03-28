## dicomReadWrite.py
#
# The purpose of this module is to define functions related to DICOM read/write operations.
#

from pydicom import dcmread
import string
import __LOG.log as log
from datetime import datetime
from random import randint, choice
import os
from tkinter import messagebox # used to display a popup if there is a logging error (messagebox.showerror).
import sqlite3


## Connect to local DICOM Databases
attributes = os.getcwd() + "\\db\\attributes.db"
db_attributes = sqlite3.connect(attributes)
cur_attributes = db_attributes.cursor()


## DICOM Static Variables
impClassUID = "1.2.7238.7553.751998.970815"


## Functions for Writing to Files
def create_dcm_file_dir():
    newFilePathDCM = os.getcwd() + "\\DICOM Files\\"
    if os.path.exists(newFilePathDCM):
        log.write_log_file(f"The file directory for DICOM files created by this program already exists: {newFilePathDCM}", 4)
    else:
        try:
            os.mkdir(newFilePathDCM)
            log.write_log_file(f"The file directory for DICOM files did not exist and has been created: {newFilePathDCM}", 4)
        except:
            messagebox.showerror("DICOM File Directory Error", f"The DICOM file directory at {newFilePathDCM} could not be created. Please check the file write permissions for the current Windows user.")
            log.write_log_file(f"The file directory at {newFilePathDCM} could not be created. New files will be created at {os.getcwd()}", 4)
            newFilePathDCM = os.getcwd()
    return newFilePathDCM


## Functions Used in DICOM Attribute Writing
def get_date_time():
    """
    Returns the current date and time, as well as the current date time.
    get_date_time()[0] = Current Date in YYMMDD format
    get_date_time()[1] = Current Time in HHmmSS format
    get_date_time()[2] = Current Date Time in UID format, so currentDate.CurrentTimeUID, 
                         where Current Time UID is in HHmmSSffffff format
    """
    currentDate = datetime.today().strftime('%Y%m%d')
    currentTime = datetime.today().strftime('%H%M%S')
    currentTimeUID = datetime.today().strftime('%H%M%S%f')
    currDateTimeUID = f"{currentDate}.{currentTimeUID}"
    return currentDate, currentTime, currDateTimeUID


def rand_int_as_str(length=8):
    randIntUID = ""
    for each in range(length):
        randIntUID = f"{randIntUID}{randint(0,9)}"
    return randIntUID


## Base DICOM Functions
def read_files(dcmFilePath):
    if len(dcmFilePath) > 0:
        log.write_log_file("Reading DICOM files.", 6)
        log.write_log_file(f"Number of DICOM Files = {len(dcmFilePath)}", 6)
        dcmFile = [None] * len(dcmFilePath)
        try:
            for file in range(len(dcmFilePath)):
                dcmFile[file] = dcmread(dcmFilePath[file])
                log.write_log_file(f"Read DICOM contents of {dcmFilePath[file]} to 'dcmFile' array at index {file}", 6)
                if file == (len(dcmFilePath))-1:
                    log.write_log_file("All DICOM files have been read successfully.",6)
        except:
            log.write_log_file("Exception thrown when attempting to read DICOM files.", 3)


def rand_UI(length=44, prefixImpClassUID = 0):
    if prefixImpClassUID != 0:
        prefixUID = impClassUID + "." + rand_int_as_str(5)
    else:
        randPrefixUID = "1.2." + f"{rand_int_as_str(3)}" + "." + f"{rand_int_as_str(5)}"
        prefixUID = randPrefixUID + "." + rand_int_as_str(5)
    randUID = prefixUID + "." + get_date_time()[2]
    if len(randUID) % 2 != 0:       # DICOM conformity for the UI VR is to have the value be even. If odd, tack on a random number at the end.
        randUID = randUID + rand_int_as_str(1)
    return randUID


def rand_PN():
    """
    Output an anonymized name in the DICOM format for the PN value representation
        randName = anonLast####^anonFirst####
    """
    randNum = rand_int_as_str(4)
    last = "anonLast" + randNum
    first = "anonFirst" + randNum
    randName = f"{last}^{first}"
    return randName


def rand_DA_TM_DT(yrsPast = 10, yrsFuture = 0):
    currYear = get_date_time()[0][:4]
    minYear = int(currYear) - yrsPast
    maxYear =  int(currYear) + yrsFuture
    randDA = f"{randint(minYear,maxYear)}" + "0101"
    randTM = f"{randint(00, 12):02d}" + "0000"
    randDT = randDA + randTM
    return randDA, randTM, randDT

def rand_SH_ST_LO_UC(length = 12):
    char = string.ascii_letters + string.digits
    randVal = ""
    for each in range(length):
        randVal = f"{randVal}{choice(char)}"
    print(randVal)
    return randVal


## DICOM functions called in conjunction with the Base DICOM Functions
def anonymize_data(dcmFilePath):
    """
    https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_e.html
    """
    read_files(dcmFilePath)
    # anonymize files here


