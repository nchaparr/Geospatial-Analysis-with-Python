import math
x1=456456.23
y1=1279721.064
x2=576628.34
y2=1071740.33
x_dist=x1-x2
y_dist=y1-y2
dist_sq=x_dist**2 + y_dist**2
distance=math.sqrt(dist_sq)
print(distance)

X1=-90.21
Y1=32.31
X2=-88.95
Y2=30.43
X_dist=math.radians(X1-X2)
Y_dist=math.radians(Y1-Y2)
Dist_sq=X_dist**2 + Y_dist**2
Dist_rad=math.sqrt(Dist_sq)
print(Dist_rad*6371251.46)

