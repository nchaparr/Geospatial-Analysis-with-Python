from dbfpy3 import dbf
from osgeo import gdal
from osgeo import gdal_array
try:
    import Image
    import ImageDraw
except:
    from PIL import Image
    from PIL import ImageDraw
import shapefile
import geopandas
import matplotlib.pyplot as plt
import pymysql


conn=pymysql.connect(host='localhost',port=3306, user='root',passwd='',db='mysql')
cur=conn.cursor()
cur.execute("DROP DATABASE IF EXISTS spatial_db")
cur.execute("CREATE DATABASE spatial.db")
cur.close()
conn.close()

conn=pymysql.connect(host='localhost', port=3306, user='root',passwd='',db='spatial_db')
cur=conn.cursor()
cur.execute("CREATE TABLE PLACES (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, Name varchar(50) NOT NULL, location Geometry NOT NULL)")
cur.execute("INSERT INTO PLACES (name, location) VALUES ('NEW ORLEANS',GeomFromText('POINT(30.03 90.03)'))")
cur.execute("INSERT INTO PLACES (name, location) VALUES ('MEMPHIS', GeomFromText('POINT(35.05 90.00)'))")

p1,p2 = [p[0] for p in cur.fetchall()]
cur.execute("SET @p1=ST_GeomFromText('{}')".format(p1))
cur.execute("SET @p2=ST_GeomFromText('{}')".format(p2))
cur.execute("SELECT ST_Distance(@p1,@p2")
d=float(cur.fetchone()[0])

print(d)
#print("{:.2f} miles from New Orleans to Memphis".format(d*70))

cur.close()
conn.close()

gdf=geopandas.GeoDataFrame
census=gdf.from_file("GIS_CensusTract_poly.shp")
census.plot()
plt.show()


r=shapefile.Reader("hancock.shp")
xdist=r.bbox[2]-r.bbox[0]
ydist=r.bbox[3]-r.bbox[1]
iwidth=400
iheight=600
xratio=iwidth/xdist
yratio=iheight/ydist
pixels=[]
for x,y in r.shapes()[0].points:
    px=int(iwidth - ((r.bbox[2]-x)*xratio))
    py=int((r.bbox[3]-y)*yratio)
    pixels.append((px,py))

img=Image.new("RGB",(iwidth,iheight),"white")
draw=ImageDraw.Draw(img)
draw.polygon(pixels,outline="rgb(203,196,190)",fill="rgb(198,204,189)")
img.save("hancock.png")
Image.open("hancock.png").show()

srcArray=gdal_array.LoadFile("SatImage.tif")
band1=srcArray[0]
gdal_array.SaveArray(band1, "band1.jpg",format="JPEG")

raster=gdal.Open("SatImage.tif")
print(raster.RasterCount)
print(raster.RasterXSize)
print(raster.RasterYSize)

db=dbf.Dbf("GIS_CensusTract_poly.dbf")
print(db[0])
rec=db[0]
field=rec["POPULAT10"]
rec.store()
del rec
print(db[0]["POPULAT10"])


