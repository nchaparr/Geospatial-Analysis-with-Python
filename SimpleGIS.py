import turtle as t

NAME = 0
POINTS = 1 
POP = 2

state = ["COLRADO", [[-109,37], [-109,41], [-102,41], [-102,37]], 5187582]

cities = []
cities.append(['DENVER', [-104.98,39.74],634265])
cities.append(['BOULDER', [-105.27,40.02],98889])
cities.append(['DENVER', [-107.88,37.28],17069])

map_width = 400
map_height = 300

minx=180
maxx=-180
miny=90
maxy=-90

for x,y in state[POINTS]:
    if x<minx:minx=x
    elif x>maxx:maxx=x
    elif y>maxy:maxy=y

dist_x=maxx-minx
dist_y=maxy-miny
x_ratio=map_width/dist_x
y_ratio=map_height/dist_y

def convert(point):
    lon=point[0]
    lat=point[1]
    x=map_width-((maxx-lon)*x_ratio)
    y=map_height-((maxy-lat)*y_ratio)
    x=x-(map_width/2)
    y=y-(map_height/2)
    return [x,y]


t.up()
first_pixel=None
for point in state[POINTS]:
    pixel=convert(point)
    if not first_pixel:
        first_pixel=pixel
    t.goto(pixel)
    t.down()
t.goto(first_pixel)
t.up()
t.goto([0,0])
t.write(state[NAME],
align="center",
font=("Arial",16,"bold"))

t.done()
