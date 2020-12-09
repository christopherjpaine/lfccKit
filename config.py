
class Config:
    ### Configuration

    ## Size and Shape of Regions

    # Canvas size 
    canvasWidthPx = 500
    canvasHeightPx = 500

    # average size of region
    regionSizePx = 20

    # Regularity of region Lower = more irregular.
    # canvasSize/regionSize is the most reasonable minimum regularity otherwise the 
    # noise is larger than the canvas itself. Very regular (<1px irregularity)
    # is acheived around canvasSize*regionSize
    regionRegularity = 0.5

    ## Fade and Coloring

    # List of colors
    colorList = ['black', 'lightgray', 'darkgray', 'none']

    # Enabled Fade Coloring
    fadeEnabled = True

    # Fade diffusion, how far past the outside of its region do we expect to see 
    # a given color (0 very little, no real maximum)
    fadeDiffusion = 0.4

    # Size of fade region relative to the size of the whole image (1 = across full image, 0 = very centre only)
    fadeSize = 0.5

    ### Calculations
    #xDim
    xNumRegions = round(canvasWidthPx / regionSizePx)
    yNumRegions = round(canvasHeightPx / regionSizePx)
    totalNumRegions = xNumRegions * yNumRegions