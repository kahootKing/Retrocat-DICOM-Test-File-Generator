##
## Define the default dictionaries in use by the application for configurations.
## 

import xml.etree.ElementTree as ET
from types import SimpleNamespace

## Default Configuration for Generating new Test Files

default_attributes = {
        "00020010": # Transfer Syntax UID (default, Implicit VR Little Endian)
                    ["val",
                    "1.2.840.10008.1.​2"],
        "00080005": # Specific Character Set (default character set)
                    ["val",
                    "ISO_IR 6"],
        "00080016": # SOP Class UID (Digital X-Ray Image Storage - For Presentation)
                    ["val",
                    "1.2.840.10008.5.1.4.1.1.1.1"],
        "00080016": # SOP Class UID (Digital X-Ray Image Storage - For Presentation)
                    ["val",
                        "1.2.840.10008.5.1.4.1.1.1.1"],
        "00080020": ## Study Date, DA [1] Value [2] *Y* year, *M* month, or *D* day [3] *P* past or *F* future
                    ["rand",
                    "5",
                    "Y",
                    "P"],
        "00080030": ## Study Time, DT
                    ["rand"],
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
                    "F"]
}

default_cfg = SimpleNamespace(name = "Default Config (Program)",
                       filePath = "",
                       listOrder = 0,
                       defaultCfg = True,
                       hasDCM_SR = True,
                       diffPatientPerStudy = False,
                       numStudies = 1,
                       numSeries = [1],             # each val in the brackets corresponds to the numStudies
                       numInstances = [1],          # number of images per series.  Could be rand.
                       numFrames = ["rand", 1, 1],  # num frames per Instance. If [0] is "rand", treat [1] and [2] as lower & upper bound. Otherwise, length should match sum of numInstances
                       attributes = default_attributes)


## Definitions for Reading/Writing Config Files
def conv_namespace_to_xml(namespace, rootName = "config"):
    cfgXML = ET.Element(rootName)
    for key in vars(namespace):
        key_xml = ET.SubElement(cfgXML,key)
        namespace_key = getattr(namespace, key)
        if isinstance(namespace_key,dict):  ## dictionary
            for val in namespace_key:
                subkey_xml = ET.SubElement(key_xml, key, value= f"{val}") 
                attr_list = namespace_key[val]
                for each in attr_list:
                    subkey2_xml = ET.SubElement(subkey_xml,"elem")
                    subkey2_xml.text = str(each)
        else:
            key_xml.text = str(namespace_key)
    
    return cfgXML


cfgXML = conv_namespace_to_xml(default_cfg)
ET.indent(cfgXML,space="\t", level=0)
print(ET.tostring(cfgXML,encoding="unicode", method="xml"))