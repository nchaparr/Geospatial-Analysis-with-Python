import shapefile
shp=shapefile.Reader("point.shp")
shapes=shp.shapes()
records=shp.shapeRecords()
for feature in records:
    point = feature.shape.points
    rec=feature.record
    #print(point[0],point[1],rec)
    print(point,rec)

