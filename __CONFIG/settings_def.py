##
## Define the default dictionaries in use by the application for configurations.
## 

import xml.etree.ElementTree as ET

## Default Configuration (default.cfg) for Generating new Test Files

defaultCfg_backup = {
    "filePath": "",
    "name": "Default (Program Backup)",
    "listOrder": 0,
    "defaultConfig": True,
    "hasDCM_SR": False,
    "diffPatientPerStudy": False,
    "numStudies": 1,
    "numSeries": [1],        # each val in the brackets corresponds to the numStudies
    "numInstances": [1],     # number of images per series.  Could be rand.
    "numFrames": ["rand",    # num frames per Instance. If [0] is "rand", treat [1] and [2] as lower & upper bound. Otherwise, length should match sum of numInstances
                   1,
                   1],
    "globalAttr": {
                 "00020010": # Transfer Syntax UID (default, Implicit VR Little Endian)
                            ["val",
                             "1.2.840.10008.1.​2"],
                 "00080005": # Specific Character Set (default character set)
                            ["val",
                             "ISO_IR 6"],
                 "00080016": # SOP Class UID (Digital X-Ray Image Storage - For Presentation)
                            ["val",
                             "1.2.840.10008.5.1.4.1.1.1.1"],
                 "00080020": ## Study Date, DA [1] Value [2] *Y* year, *M* month, or *D* day [3] *P* past or *F* future
                            ["rand",
                             "5",
                             "Y",
                             "P"],
                 "00080030": ## Study Time, DT [1] AM or PM
                            ["rand",
                             "A"],
                 "00080060": ## Modality , can be a range of modalities for multiple studies.
                            ["val",
                             "DX"],
                 "00080050": ## Accession Number
                            ["rand"],
                 "00100010": ## Patient's Name
                            ["rand"],
                 "00100020": ## Patient ID
                            ["rand"],
                 "00100030": ## Patient DOB
                            ["val",
                             "19800808"],
                 "00100030": ## Patient Sex
                            ["val",
                             "F"],         
                 }
}