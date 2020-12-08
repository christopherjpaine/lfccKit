
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.spatial import Voronoi, voronoi_plot_2d
import svgwrite
from svgwrite import cm, mm

# Custom region class
import region

### Configuration
# TODO these should be derived from grid size and canvas size and passed in from command line
# xy dims as number of regions
xDim = 40
yDim = 40
# average size of region
gridSpace = 150
# Regularity as a ratio of the grid spacing
regionRegularity = 0.5

# fade diffusion
diffusion = 0.3
# rate of fade - relative size of the fade region (1 = across full image, 0 = no fade)
fadeRate = 0.25
# List of colors to use in the central part of the fade
fadeColors = ['lightgray', 'darkgrey']

# Set to True to enable debug prints
debug = False

# Calculated from config
numPoints = xDim * yDim
fadeEdgeA = 1.5 - (1.5*fadeRate)
fadeEdgeB = 1.5 + (1.5*fadeRate)

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
            xOffset = random.gauss(0, gridSpace*regionRegularity)
            yOffset = random.gauss(0, gridSpace*regionRegularity)
            points[i,j,:] = [x+xOffset,y+yOffset]
            y += gridSpace
        y = 0
        x += gridSpace

    points = points.reshape((xDim*yDim,2))
    return points


def getColor():
    colors = ['black', 'black', 'darkgrey', 'none']
    return random.choice(colors)

def getFadeColor(index, maximum):
    ratio = (index/(numPoints-1))
    value = random.gauss((ratio*3), diffusion)
    if value <= fadeEdgeA:
        return 'black'
    elif value <= fadeEdgeB:
        #return 'grey'
        return random.choice(fadeColors)
    else:
        return 'white'

if __name__ == '__main__':

    # Generate points
    points = generatePoints(xDim, yDim, gridSpace)
    if debug and 0:
        print(points)

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
    if debug and 0:
         # Voronoi gives array of all vertices (Voronoi.vertices)
        print(vor.vertices)
        # An array of regions is provided (Voronoi.regions)
        print(vor.regions)
        # Each region in the array is described as an array of indexes that correspond to the array of vertices
        # The order regions appear in the region array is given by a 1d array (Voronoi.point_region)
        print(vor.point_region)
    
    # Set the region vertices
    # Iterate through pointRegion array
    for i in range(len(regionList)):
        regionIndex = vor.point_region[i]
        # Get correct row from region array
        regionVerticesIndexed = vor.regions[regionIndex]
        #print(i)
        # For each vertice index, append the coordinates into an array
        for vertexIndex in regionVerticesIndexed:
            # vertexIndex of negative 1 represents an edge that goes to infinity
            # We mark these because they cause artefacts in the drawing
            if vertexIndex == -1:
                regionList[i].isEdge = True
            regionList[i].appendVertex(vor.vertices[vertexIndex])

        if debug:
            # Print vertex coords of all regions
            print('region ' + str(i) + 'vertices:')
            regionList[i].printVertices()
        
        #regionList[i].setColor(getColor)
        regionList[i].setColor(getFadeColor(i, numPoints))
            
    
    if debug and 0:
        # Plot using matplotlib
        fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',line_width=3, line_alpha=0.6, point_size=2)
        plt.show()

    # Initialise the canvas
    # TODO Don't overwrite existing and add text to image/filename with the input params
    svg = svgwrite.Drawing('new.svg', size=('100cm', '100cm'), profile='full', debug=True)

    # Draw all regions
    for region in regionList:
        region.drawRegion(svg)

    svg.save()
        
