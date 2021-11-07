import fire
import cv2 as cv
from six import text_type

#Open the file by its path from CLI tryout:

src = None
def fileopen(*filename):
    src = filename + " and stuff"
    return src

if __name__== '__main__':
    fire.Fire(fileopen)