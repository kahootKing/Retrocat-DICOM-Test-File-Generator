## dicomReadWrite.py
#
# The purpose of this module is to define functions related to DICOM read/write operations.
#

from pydicom import dcmread
import __LOG.log as log
from datetime import datetime
from random import randint


## DICOM Static Variables
impClassUID = "1.2.7238.7553.751998"


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


## DICOM functions called in conjunction with the Base DICOM Functions
def anonymize_data(dcmFilePath):
    read_files(dcmFilePath)
    # anonymize files here