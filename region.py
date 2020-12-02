
class Region:
    _index = 0
    def __init__(self):
        Region._index += 1
        self.id = Region._index

# Set

    # Set Origin Point
    # @param origin tuple of the coordinates for the point at the "centre" of the region
    def setOrigin (self, origin):
        self.origin = origin

    # Set region vertices
    # take in an numpy array of coordinates and store them as a list of tuples
    # @param vertices numpy array of coordinates that plot the edge of the region
    def setVertices (self, vertices):
        # convert numpy array to list of tuples
        self.vertices = convertedVertices

    # Set Color
    # Set the color in whichever format is taken by drawsvg
    # @param [in]
    def setColor (self, color):
        self.color = color

# Draw

    # Draw by adding a polyline object to the svg layer
    # @param dwg layer object
    def drawRegion (self, dwg):
        dwg.add(svg.polyline(self.vertices, fill=self.color))

