from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as pl

r = 1
point = Point(0,0)
circle = point.buffer(r)


pl.plot(circle)
pl.show()
