from dbfpy3 import dbf
db=dbf.Dbf("GIS_CensusTract_poly.dbf")
print(db[0])
rec=db[0]
field=rec["POPULAT10"]
rec.store()
del rec
print(db[0]["POPULAT10"])


