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


