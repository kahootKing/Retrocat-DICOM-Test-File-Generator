## dicomReadWrite.py
#
# The purpose of this module is to define functions related to DICOM read/write operations.
#

from pydicom import dcmread
import __LOG.log as log

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


## DICOM functions called in conjunction with the Base DICOM Functions
def anonymize_data(dcmFilePath):
    read_files(dcmFilePath)
    # anonymize files here