import fire
import cv2 as cv

#Open the file by its path from CLI tryout:

src = None
def fileopen(filename):
    src = filename
    return src

if __name__== '__main__':
    fire.Fire(fileopen)