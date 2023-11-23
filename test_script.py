# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:08:11 2020

@author: ADMIN-PC
"""
import cv2 as cv 
from edge_detection import Canny_edge
from harris_corner_detection import Harris_corner


I = cv.imread('sunflower.jpg') #Can change the image as per users requirement
I = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

###################Canny Edge Detector#########################################

##Using my codefor Canny edge detection:
Canny_edge(I)

#Using the inbuilt function
Edges2 = cv.Canny(I, 150,50)
cv.imwrite('canny_edge_inbuilt_output.jpg', Edges2)
cv.imshow('From inbuilt canny detector', Edges2)
cv.waitKey(0)
cv.destroyAllWindows()

##################Harris Corner Detection######################################

##Using my code for Harris corner detection:
I = cv.imread('shapes.png')
I = cv.cvtColor(I, cv.COLOR_BGR2GRAY)

Harris_corner(I)
