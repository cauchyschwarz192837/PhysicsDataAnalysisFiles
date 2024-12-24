import numpy
from PIL import Image
import os
import math
import matplotlib.pyplot as plt

def BaslerRAW (File_Name):
    Data=numpy.fromfile(File_Name, dtype=numpy.uint8)
    ImageData=Data.reshape((1024,1280))
    red_tile = numpy.array([[0, 0],[0, 1]], dtype=numpy.bool_)
    green_tile_1 = numpy.array([[0, 1],[0, 0]], dtype=numpy.bool_)
    green_tile_2 = numpy.array([[0, 0],[1, 0]], dtype=numpy.bool_)
    blue_tile = numpy.array([[1, 0],[0, 0]], dtype=numpy.bool_)
    red_index_array=numpy.tile(red_tile,(512,640))
    green_index_array_1=numpy.tile(green_tile_1,(512,640))
    green_index_array_2=numpy.tile(green_tile_2,(512,640))
    blue_index_array=numpy.tile(blue_tile,(512,640))
    Red_layer=ImageData[red_index_array].reshape((512,640))
    Green_layer_1=ImageData[green_index_array_1].reshape((512,640))
    Green_layer_2=ImageData[green_index_array_2].reshape((512,640))
    Blue_layer=ImageData[blue_index_array].reshape((512,640))
    Image=numpy.empty([512,640,3], numpy.uint8)
    Image[:,:,0]=Red_layer
    Image[:,:,1]=((Green_layer_1.astype('d')+Green_layer_2.astype('d'))/2).astype('B')
    Image[:,:,2]=Blue_layer
    return Image