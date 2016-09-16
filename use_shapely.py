from shapely import wkt,geometry
from osgeo import gdal
import fiona
import pprint
print("using shapely")
wktpoly="POLYGON((0 0, 4 0, 0 4, 0 0))"
poly=wkt.loads(wktpoly)
print(poly.area)
buf=poly.buffer(5.0)
print(buf.area)
print(buf.difference(poly).area)
print("now using fiona")
f=fiona.open("GIS_CensusTract_poly.shp")
print(f.driver)
print(f.bounds)
pp=pprint.PrettyPrinter(indent=4)
pp.pprint(f.schema)
print(len(list(f)))
pp.pprint(f[1])
print("now using gdal")
raster=gdal.Open("SatImage.tif")
print(raster.RasterCount)
print(raster.RasterXSize)
print(raster.RasterYSize)
