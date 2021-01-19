
class Config:

    ## Size and Shape of Regions

    # Canvas size 
    canvasWidthPx = 500
    canvasHeightPx = 500

    # average size of region
    regionSizePx = 15

    # Regularity of region Lower = more irregular.
    # canvasSize/regionSize is the most reasonable minimum regularity otherwise the 
    # noise is larger than the canvas itself. Very regular (<1px irregularity)
    # is acheived around canvasSize*regionSize
    regionRegularity = 2

    # Grid Shape
    # 1 = Square Based. With infinite regularity this will give square regions
    # 2 = Isometric based (isometric grid but 45 degree angles instead of 30). With 
    #       infinite regularity this will give hexagonal regions
    gridBaseShape = 2

    ## Fade and Coloring

    # List of colors
    # These colors will be randomly distributed when fadeEnabled is set to false.
    # When fadeEnabled is set to true the first and last colors will be at the 
    # edge and the others (known as "fade colors") will be randomly distributed
    # in the fade region.
    # example input formats -> https://www.w3.org/TR/SVGColor12/#sRGBcolor
    # predef color list -> https://www.december.com/html/spec/colorsvg.html
    colorList = ['#F0ECE6', '#5E5C5A', '#2B2827', '#0A0A0A']

    # Enabled Fade Coloring
    fadeEnabled = True

    # Fade centre 
    fadeCentre = 0.5

    # Fade diffusion, how far outside of its region do we expect to see a given color
    # From 0 to 2 seems to be the reasonable values.
    fadeDiffusion = 0.4

    # Size of fade region relative to the size of the whole image 
    # 1 = across full image, 0 = very centre only
    # Can also be thought of as the probability of the fade colors appearing.
    fadeSize = 0.25





    ### DO NOT EDIT THESE ###
    xNumRegions = round(canvasWidthPx / regionSizePx)
    yNumRegions = round(canvasHeightPx / regionSizePx)
    totalNumRegions = xNumRegions * yNumRegions