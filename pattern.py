
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.spatial import Voronoi, voronoi_plot_2d

# Configuration
xDim = 3
yDim = 3
gridSpace = 10

# From config
numPoints = xDim * yDim

# Given the dimensions of the grid and the spacing return a numpy array of coordinates
# in the shape numPoints x 2
# Currently a square grid with gauss noise added
# TODO expand to generate list of points as a circle or an offset grid, or different noises
def generatePoints(xDim, yDim, gridSpace):
    x = 0
    y = 0
    points = np.arange(xDim*yDim*2).reshape((xDim,yDim,2))
    for i in range(0,xDim):
        for j in range(0,yDim):
            xOffset = random.gauss(0,gridSpace/4)
            yOffset = random.gauss(0,gridSpace/4)
            points[i,j,:] = [x+xOffset,y+yOffset]
            y += gridSpace
        print(points[i,:])
        y = 0
        x += gridSpace

    points = points.reshape((xDim*yDim,2))
    return points


if __name__ == '__main__':

    # Generate points
    points = generatePoints(xDim, yDim, gridSpace)
    
    # Initialise list of regions
    regionList = []
    for i in range(0, numPoints):
        regionList.append( Region() )

    # Set origin of each region
    for region in regionList:
        region.setOrigin(points[region.id])

    # generate voronoi from numpy array of points
    vor = Voronoi(points)

    # Plot voronoi for debug
    fig = voronoi_plot_2d(vor)
    #    fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',line_width=3, line_alpha=0.6, point_size=2)
    plt.show()

    # Set the region vertices
        # Voronoi gives array of all vertices (Voronoi.vertices)
        # An array of regions is provided (Voronoi.regions)
        # Each region in the array is described as an array of indexes that correspond to the array of vertices
        # The order regions appear in the region array is given by a 1d array (Voronoi.point_region)
        
        # Iterate through pointRegion array
            # Get Region object
            # Get correct row from region array
            # Set vertices in region object

    # Iterate through all regions
        # Assign color to each (Should do this in the init of the object)