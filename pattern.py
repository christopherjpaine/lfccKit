
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.spatial import Voronoi, voronoi_plot_2d
import svgwrite
import sys
from shutil import copyfile
from datetime import datetime
from svgwrite import cm, mm


# Custom region class
import region

# Config file
from config import Config

# Set to True to enable debug prints
debug = False

# fade positions
fadeEdgeA = 1 - (1*Config.fadeSize)
fadeEdgeB = 1 + (1*Config.fadeSize)

# Given the dimensions of the grid and the spacing return a numpy array of coordinates
# in the shape numPoints x 2
# Currently a square grid with gauss noise added
# TODO expand to generate list of points as a circle or an offset grid, or different noises
def generatePoints(xDim, yDim, gridSpace, gridRegularity):
    x = 0
    y = 0
    points = np.arange(xDim*yDim*2).reshape((xDim,yDim,2))
    for i in range(0,xDim):
        for j in range(0,yDim):
            xOffset = random.gauss(0, gridSpace/gridRegularity)
            yOffset = random.gauss(0, gridSpace/gridRegularity)
            points[i,j,:] = [x+xOffset,y+yOffset]
            y += gridSpace
        y = 0
        x += gridSpace

    points = points.reshape((xDim*yDim,2))
    return points


def getColor():
    return random.choice(Config.colorList)

def getFadeColor(index, maximum):
    ratio = (index/(maximum-1))
    value = random.gauss((ratio*3), Config.fadeDiffusion)
    if value <= fadeEdgeA:
        return Config.colorList[0]
    elif value <= fadeEdgeB:
        #return 'grey'
        return random.choice(Config.colorList[1:-1])
    else:
        return Config.colorList[-1]

if __name__ == '__main__':

    # Generate points
    points = generatePoints(Config.xNumRegions, Config.yNumRegions, Config.regionSizePx, Config.regionRegularity)
    if debug and 1:
        print(points)

    # Initialise list of regions
    regionList = []
    for i in range(0, Config.totalNumRegions):
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

        if debug and 0:
            # Print vertex coords of all regions
            print('region ' + str(i) + ' vertices:')
            regionList[i].printVertices()
        
        if Config.fadeEnabled:
            regionList[i].setColor(getFadeColor(i, Config.totalNumRegions))
        else:
             regionList[i].setColor(getColor())

    if debug and 0:
        # Plot using matplotlib
        fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',line_width=3, line_alpha=0.6, point_size=2)
        plt.show()

    # Initialise the canvas
    # TODO Don't overwrite existing and add text to image/filename with the input params
    svg = svgwrite.Drawing('output.svg', size=(Config.canvasWidthPx, Config.canvasHeightPx), profile='full', debug=True)

    # Draw all regions
    for region in regionList:
        region.drawRegion(svg)

    svg.save()

    # Move svg and copy of configs to output folder

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        #now = datetime.now()
        #filename = now.strftime("%d%m%Y_%H%M%S")
        filename = 'size' + str(Config.regionSizePx) + '_regu' + str(Config.regionRegularity)
        if (Config.fadeEnabled):
            fadeString = '_fade' + str(Config.fadeSize) + '_diff' + str(Config.fadeDiffusion)
            filename = filename + fadeString
        sizeString = '[' + str(Config.canvasHeightPx) + 'x' + str(Config.canvasWidthPx) + ']'
        filename = filename + sizeString
        filename = filename.replace('.', '_')


    filename = 'outputs/' + filename
    copyfile('output.svg', filename+'.svg')
    copyfile('config.py', filename+'.config')

        
