# This tool takes in two inputs:
#      (1) CSV file of ALL DICOM attributes, which should have no header & match the attr.db file from the Retrocat application.
#      (2) CSV file of all DICOM attributes that have an anonymized value based on the Basic Profile (https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1)
#
# The output of this tool is a printed list (in CSV format) of ALL attributes & their respective anonymized value (if present).

import csv

anon_dict = []
attr_dict = []

with open('C:\\Users\\alyss\\Downloads\\anon.csv', mode='r') as anonFile:
    anon = csv.reader(anonFile)
    for row in anon:
        anon_dict.append(row)

with open('C:\\Users\\alyss\\Downloads\\attr.csv') as attrFile:
    attr = csv.reader(attrFile)
    for row in attr:
        attr_dict.append(row)

row = 0

for row in range(len(anon_dict)):
    anonAttr = anon_dict[row][0]
    anonVal = anon_dict[row][1]
    for row in range(len(attr_dict)):
        if attr_dict[row][0] == anonAttr:
           ## write anonVal to attr_dict[z][5]
           attr_dict[row][5] = anonVal
           break

for attrRow in range(len(attr_dict)):
    print(attr_dict[attrRow][0] + "," + attr_dict[attrRow][5])