
class Config:

    ## Size and Shape of Regions

    # Canvas size 
    canvasWidthPx = 5000
    canvasHeightPx = 2500

    # average size of region
    regionSizePx = 50

    # Regularity of region Lower = more irregular.
    # canvasSize/regionSize is the most reasonable minimum regularity otherwise the 
    # noise is larger than the canvas itself. Very regular (<1px irregularity)
    # is acheived around canvasSize*regionSize
    regionRegularity = 5

    ## Fade and Coloring

    # List of colors
    # These colors will be randomly distributed when fadeEnabled is set to false.
    # When fadeEnabled is set to true the first and last colors will be at the 
    # edge and the others (known as "fade colors") will be randomly distributed
    # in the fade region.
    # example input formats -> https://www.w3.org/TR/SVGColor12/#sRGBcolor
    # predef color list -> https://www.december.com/html/spec/colorsvg.html
    colorList = ['#FFFFFF', '#CCCCCC', '#808080', '#606060', '#404040', '#202020']

    # Enabled Fade Coloring
    fadeEnabled = True

    # Fade diffusion, how far outside of its region do we expect to see a given color
    # From 0 to 2 seems to be the reasonable values.
    fadeDiffusion = 0.3

    # Size of fade region relative to the size of the whole image 
    # 1 = across full image, 0 = very centre only
    # Can also be thought of as the probability of the fade colors appearing.
    fadeSize = 0.18





    ### DO NOT EDIT THESE ###
    xNumRegions = round(canvasWidthPx / regionSizePx)
    yNumRegions = round(canvasHeightPx / regionSizePx)
    totalNumRegions = xNumRegions * yNumRegions