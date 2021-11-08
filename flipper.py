from __future__ import print_function
import fire
import cv2 as cv
import sys
import numpy as np
from pathlib import Path

#Our standard entry point: it takes our CLI input, passes it to the actual working function, recieves the result from it and returns the result

def main_(source_path: str, text: str = "", save_path = None):
    res = do_flip(source_path=source_path, text=text, save_path=save_path)
    return res

#This function actually does the work       

def do_flip(source_path: str, text: str = "", save_path = None):
   
   #Open the file by its name and path from CLI:
    src = cv.imread(cv.samples.findFile(source_path))
    if src is None:
        raise ValueError(f"File not found: {source_path}")
   
    #Creating image map for the source image    

    map_x = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)
    map_y = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32)

    #Flipping the image

    flip_map(map_x, map_y)
    dst = cv.remap(src, map_x, map_y, cv.INTER_LINEAR)

    #If there's a text to write on image, write it now
    
    center_x = int(len(map_x)/2)
    center_y = int(len(map_y)/2)
    org = (center_x, center_y)
    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 1;
    color = (220,220,220)
    thickness = 2

    if not text=="":
        cv.putText(dst, text, org, font, font_scale, color, thickness)

    if not save_path:

        #Popping up the window with the resulting image for 3 seconds

        window_name = 'Remap demo'
        cv.namedWindow(window_name)
        cv.imshow(window_name, dst)
        cv.waitKey(3000)

        #Saving the resulting image to the file

    else:
        Path(save_path).absolute().parent.mkdir(exist_ok=True, parents=True) #ensure that path exist
        is_written = cv.imwrite(save_path, dst)
        if not is_written:
            raise ValueError(f"Failed to write: {save_path}")
        print(f"Saved to {save_path}")

#Flipping function from https://docs.opencv.org/4.x/d1/da0/tutorial_remap.html

def flip_map(map_x, map_y):
    for i in range(map_x.shape[0]):
        map_x[i,:] = [x for x in range(map_x.shape[1])]
    for j in range(map_y.shape[1]):
        map_y[:,j] = [map_y.shape[0]-y for y in range(map_y.shape[0])]


if __name__== '__main__':
    fire.Fire(main_)



