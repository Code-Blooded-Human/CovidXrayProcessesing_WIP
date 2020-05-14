# versiom 0.0.1
# Draw bounding boxes on JPEG images 
# author: Abhishek Shingane abhisheks@iitbhilai.ac.in
# Requirements
# Pillow:
#   Image Manipulation Library forked from PIL
#   pip3 install --upgrade Pillow


import sys
import os
from PIL import Image, ImageDraw

standardReferenceImageSize = [224,224]

def scaleCoordinates(boundingCoordinates,imageSize,referenceImageSize):
    #boundingCoordinates is array [top left x, top left y, bottom right x,bottom right y]
    #imageSize and referenceImageSize is array [width,height in px]
    newBoundingCoordinates = [0,0,0,0]
    newBoundingCoordinates[0] = (imageSize[0]*boundingCoordinates[0])/referenceImageSize[0]
    newBoundingCoordinates[1] = (imageSize[1]*boundingCoordinates[1])/referenceImageSize[1]
    newBoundingCoordinates[2] = (imageSize[0]*boundingCoordinates[2])/referenceImageSize[0]
    newBoundingCoordinates[3] = (imageSize[1]*boundingCoordinates[3])/referenceImageSize[1]
    return newBoundingCoordinates


def drawBoundingBox(srcUrl,boundingCoordinates,destUrl="out.jpeg",referenceImageSize=standardReferenceImageSize):
    try:
        rawImage = Image.open(srcUrl)
    except FileNotFoundError as err:
        print("Couldnot open or find file: "+srcUrl)
        exit()
    imageSize=[rawImage.size[0],rawImage.size[1]] #Width Height
    resizedBoundingCoordinates = scaleCoordinates(boundingCoordinates,imageSize,referenceImageSize)
    draw = ImageDraw.Draw(rawImage)
    draw.rectangle(resizedBoundingCoordinates)
    del draw
    rawImage.save(destUrl)

drawBoundingBox("./assets/test_xra831x1024.jpeg",[10,10,100,100],"out.jpeg")
