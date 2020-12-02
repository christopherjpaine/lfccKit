#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 07.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite
from svgwrite import cm, mm   
import random

colors = ['black', 'black', 'darkgrey', 'none']

svg = svgwrite.Drawing()

def getColor():
    return random.choice(colors)

def addCircle(dwg, centre, radius):
    dwg.add(svg.circle(centre, radius))

def addGridCircles(dwg, repeats, originInitial, spacing, radius):
    circleGrid = dwg.add(svg.g(id='circleGrid'))
    origin = originInitial
    for i in range(repeats):
        for j in range(repeats):
            if (j % 2) == 0:
                addCircle(circleGrid, origin, radius)
            else:
                addCircle(circleGrid, (origin[0], origin[1]+(spacing/2)), radius)
            origin = list(origin)
            origin[0] += spacing
            origin = tuple(origin)
        origin = list(origin)
        origin[1] += spacing
        origin[0] = originInitial[0]
        origin = tuple(origin)

def layer_Circles():
    circleLayer = svg.add(svg.g(id='circleLayer', fill='none', stroke='lightgray', stroke_width=5))
    addGridCircles(circleLayer, 20, (-100,-100), 500, 200)

def addParagram(dwg, origin, xlen, ylen, ratio, fill):
    x1 = origin[0]
    x2 = origin[0]+xlen
    y1 = origin[1]
    y12 = origin[1]+(ylen * ratio)
    y2 = origin[1]+ylen
    y21 = origin[1]+(ylen * (1 - ratio))
    points = [(x1,y1),(x1,y12),(x2,y2),(x2,y21)]
    dwg.add(svg.polyline(points, fill=fill))

def addZigZag(dwg, repeats, origin, ylen):
    zigzag = dwg.add(svg.g(id='row'))
    xlen = ylen * 0.8
    for i in range(repeats):
        if (i % 2) == 0:
            addParagram(zigzag, origin, xlen, ylen, 0.5, getColor())
        else:
            addParagram(zigzag, (origin[0],origin[1]+ylen), xlen, -ylen, 0.5, getColor())
        origin = list(origin)
        origin[0] += xlen
        origin = tuple(origin)

def layer_ZigZag():
    zigzagLayer = svg.add(svg.g(id='zigzagLayer'))
    origin = (-100,-100)
    size = 500
    for i in range(30):
        addZigZag(zigzagLayer, 20, origin, size)
        origin = list(origin)
        origin[1] += size/2
        origin = tuple(origin)

def layer_OffsetZigZag():
    offsetLayer = svg.add(svg.g(id='offsetLayer'))
    origin = (-50,-50)
    size = 500
    for i in range(30):
        addZigZag(offsetLayer, 20, origin, size)
        origin = list(origin)
        origin[1] += size/2
        origin = tuple(origin)

def addZigZagSpaced(dwg, repeats, origin, ylen):
    zigzag = dwg.add(svg.g(id='row'))
    xlen = ylen * 0.8
    spacing = xlen
    for i in range(repeats>>1):
        addParagram(zigzag, origin, xlen, ylen, 0.5, getColor())
        origin = list(origin)
        origin[0] += xlen
        origin = tuple(origin)
        addParagram(zigzag, (origin[0],origin[1]+ylen), xlen, -ylen, 0.5, getColor())
        origin = list(origin)
        origin[0] += xlen + spacing
        origin = tuple(origin)

def layer_ZigZagSpaced():
    zigzagLayer = svg.add(svg.g(id='zigzagLayer'))
    origin = (-100,-100)
    size = 500
    for i in range(30):
        addZigZagSpaced(zigzagLayer, 20, origin, size)
        origin = list(origin)
        origin[1] += size
        origin = tuple(origin)

def layer_slick():
    None

def addSlick(dwg, origin, xlen, ylen):
    end = (origin[0]+xlen, origin[1]+ylen)
    dwg.add(svg.path([origin, end]), stroke='black')

if __name__ == '__main__':
    svg = svgwrite.Drawing('pattern.svg', size=('100cm', '100cm'), profile='full', debug=True)
    layer_Circles()
    layer_ZigZag()
    #layer_ZigZagSpaced()
    #layer_OffsetZigZag()
    svg.save()