# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:21:38 2020

@author: ADMIN-PC
"""

import numpy as np
import cv2 as cv

def Harris_corner(I):
    row,col = I.shape
    
    ##Sobel filters
    sobel_x = [[-1,-2,-1], [0, 0, 0], [1, 2, 1]]
    sobel_x = np.array(sobel_x)
        
    sobel_y = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = np.array(sobel_y)
    
    ##Step-1 Calculating the gradients required:
    Ig = cv.GaussianBlur(I , (3,3), 0)
    Ix = cv.filter2D(Ig,-1,sobel_x)
    Iy = cv.filter2D(Ig,-1,sobel_y)
    
    ##Step-2 Getting the squares of the array elements:
    Ixx = Ix**2
    Iyy = Iy**2
    Ixy = Ix*Iy
    
    ##Step-3 convoluting with box filter:
    Ixxg = cv.boxFilter(Ixx,-1,(3,3))
    Iyyg = cv.boxFilter(Iyy,-1,(3,3))
    Ixyg = cv.boxFilter(Ixy,-1,(3,3))
    
    ##Step-4 Calculating the R values and deciding the corners:
    M = np.zeros((2,2)) 
    k = 0.06
    Ic = np.zeros((row,col))
    for i in range(0,row):
        for j in range(0,col):
            M[0,0] = (Ixxg[i,j])**2
            M[0,1] = Ixyg[i,j]**2
            M[1,0] = (Iyyg[i,j])**2
            M[1,1] = Ixyg[i,j]**2
            eig_1, eig_2 = np.linalg.eigvals(M)
            R = (eig_1*eig_2) - (k*((eig_1+eig_2)**2))
            if R > 0:
                Ic[i,j] = 255
    
    ##Showing the output
    cv.imwrite('harris_corner_output.jpg', Ic.astype('uint8'))
    cv.imshow('harris_corner_output', Ic.astype('uint8'))
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    return Ic.astype('uint8')

