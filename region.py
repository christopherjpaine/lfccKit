
import svgwrite

svg = svgwrite.Drawing()

class Region:
    _index = 0
    
    def __init__(self):
        self.id = Region._index
        Region._index += 1
        self.vertices = list()
        self.isEdge = False


# Set

    # Set Origin Point
    # @param origin tuple of the coordinates for the point at the "centre" of the region
    def setOrigin (self, origin):
        self.origin = origin

    # Add a vertex to the region
    def appendVertex (self, vertex):
        # convert numpy array to list of tuples
        tupleVertex = tuple(vertex)
        self.vertices.append(tupleVertex)

    def printVertices ( self ):
        for vertex in self.vertices:
            print('('+str(vertex[0])+','+str(vertex[1])+'),', end='')
        print()

    # Set Color
    # Set the color in whichever format is taken by drawsvg
    # @param [in]
    def setColor (self, color):
        self.color = color

# Draw

    # Draw by adding a polyline object to the svg layer
    # @param dwg layer object
    def drawRegion (self, dwg):
        if not self.isEdge:
            dwg.add(svg.polyline(self.vertices, fill=self.color))
       
