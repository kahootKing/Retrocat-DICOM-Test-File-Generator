# uses SQLite

import pandas
import sqlalchemy

dcmCSV = 'C:\\Users\\alyss\\Downloads\\DICOMAttributes_uptoAnonOnly.csv'
dcmDB = 'sqlite:///dcm.db'
engine = sqlalchemy.create_engine(dcmDB)

readCSV = pandas.read_csv(dcmCSV)
readCSV.to_sql(name = "attributes",
               con = engine,
               if_exists="replace",
               index=False)