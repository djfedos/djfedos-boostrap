from __future__ import print_function
import fire
import cv2 as cv
import sys
import numpy as np

#Flipping function from https://docs.opencv.org/4.x/d1/da0/tutorial_remap.html

def flip_map(map_x, map_y):
    for i in range(map_x.shape[0]):
        map_x[i,:] = [x for x in range(map_x.shape[1])]
    for j in range(map_y.shape[1]):
        map_y[:,j] = [map_y.shape[0]-y for y in range(map_y.shape[0])]

#Open the file by its path from CLI:

src = None
def fileopen(filename):
    global src
    src = cv.imread(cv.samples.findFile(filename))
    if src is None:
        sys.exit("File not found")

if __name__== '__main__':
    fire.Fire(fileopen)

#Creating image map for the source image    

map_x = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)
map_y = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)

#Popping up the window

window_name = 'Remap demo'
cv.namedWindow(window_name)

#Outputing the flipped image to the window, holding it up for 10 seconds

flip_map(map_x, map_y)
dst = cv.remap(src, map_x, map_y, cv.INTER_LINEAR)
cv.imshow(window_name, dst)
cv.waitKey(10000)


