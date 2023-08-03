# -*- coding: utf-8 -*-
"""image sketching using cv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1usQx0Rt3emJvGdJJWLEL3-qglYDbFFtZ
"""

import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
import numpy as np
image = io.imread("/content/lion.jpg")
cv2_imshow(image)

grey_filter = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv2_imshow(grey_filter)

invert=cv.bitwise_not(grey_filter)
cv2_imshow(invert)

blur=cv.GaussianBlur(invert,(21,21),0)
cv2_imshow(blur)

invertedblur=cv.bitwise_not(blur)
cv2_imshow(invertedblur)

sketch_filter=cv.divide(grey_filter,invertedblur,scale=225.0)
cv2_imshow(sketch_filter)
cv.imwrite("9.jpg",sketch_filter)