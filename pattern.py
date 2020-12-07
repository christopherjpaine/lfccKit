
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.spatial import Voronoi, voronoi_plot_2d
import svgwrite
from svgwrite import cm, mm

# Custom region class
import region

# Configuration
xDim = 20
yDim = 20
gridSpace = 50

# From config
numPoints = xDim * yDim

colors = ['black', 'black', 'darkgrey', 'none']

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
        y = 0
        x += gridSpace

    points = points.reshape((xDim*yDim,2))
    return points


def getColor():
    return random.choice(colors)


if __name__ == '__main__':

    # Generate points
    points = generatePoints(xDim, yDim, gridSpace)
    #print(points)

    # Initialise list of regions
    regionList = []
    for i in range(0, numPoints):
        newRegion = region.Region()
        regionList.append( newRegion )

    # Set origin of each region
    for region in regionList:
        region.setOrigin(points[region.id])

    # generate voronoi from numpy array of points
    vor = Voronoi(points)
    if 1:
         # Voronoi gives array of all vertices (Voronoi.vertices)
        print(vor.vertices)
        # An array of regions is provided (Voronoi.regions)
        print(vor.regions)
        # Each region in the array is described as an array of indexes that correspond to the array of vertices
        # The order regions appear in the region array is given by a 1d array (Voronoi.point_region)
        print(vor.point_region)

    # Plot voronoi for debug
    #fig = voronoi_plot_2d(vor)
    #    fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',line_width=3, line_alpha=0.6, point_size=2)
    
    # Set the region vertices
    # Iterate through pointRegion array
    for i in range(len(regionList)):
        regionIndex = vor.point_region[i]
        # Get correct row from region array
        regionVerticesIndexed = vor.regions[regionIndex]
        print(i)
        # For each vertice index, append the coordinates into an array
        for vertexIndex in regionVerticesIndexed:
            #print(vor.vertices[vertexIndex])
            if vertexIndex == -1:
                regionList[i].isEdge = True
            regionList[i].appendVertex(vor.vertices[vertexIndex])
        regionList[i].printVertices()
        regionList[i].setColor(getColor())
            
    
    #plt.show()

    svg = svgwrite.Drawing('new.svg', size=('100cm', '100cm'), profile='full', debug=True)

    # Iterate through all regions
        # Assign color to each (Should do this in the init of the object)
    for region in regionList:
        region.drawRegion(svg)

    svg.save()
        
