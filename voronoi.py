import matplotlib.pyplot as plt
import numpy as np
import random
xLength = 3
yLength = 3
points = np.zeros((xLength,yLength,2))
gridSpace = 10
x = 0
y = 0

points = np.arange(xLength*yLength*2).reshape((xLength,yLength,2))
#points = np.diag((xLength,yLength)) # Pre-allocate points
for i in range(0,xLength):
    for j in range(0,yLength):
        xOffset = random.gauss(0,gridSpace/4)
        yOffset = random.gauss(0,gridSpace/4)
        points[i,j,:] = [x+xOffset,y+yOffset]
        y += gridSpace
    print(points[i,:])
    y = 0
    x += gridSpace

points = points.reshape((xLength*yLength,2))

from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(points)
#vertices, ridge_points, ridge_vertices, regions, pointRegions 
print('points')
print(vor.vertices)
print('regions')
print(vor.regions)
print('pointRegions')
print(vor.point_region)
fig = voronoi_plot_2d(vor)
fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',
line_width=3, line_alpha=0.6, point_size=2)
plt.show()