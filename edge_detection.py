# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:36:11 2020

@author: ADMIN-PC
"""

import numpy as np
import cv2 as cv
import math
  

def Canny_edge(I):
    row, col = I.shape
    
    ##Defining Sobel filters
    sobel_x = [[-1,-2,-1], [0, 0, 0], [1, 2, 1]]
    sobel_x = np.array(sobel_x)
    
    sobel_y = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = np.array(sobel_y)
    
    ##Step-1 Getting the filtered images:
    Ig = cv.GaussianBlur(I , (3,3), 0)
    Ix = cv.filter2D(Ig,-1,sobel_x)
    Iy = cv.filter2D(Ig,-1,sobel_y)
    
    #Getting the magnitude array
    M = (Ix**2 + Iy**2)**0.5
    M = (M/np.max(M))*255
    
    #Getting the Direction array
    Di_mat = np.zeros((row,col))
    for i in range(0,row):
        for j in range(0,col):
            if Ix[i,j] == 0:
                continue
            else:
                Di_mat[i,j] = (math.atan(Iy[i,j]/Ix[i,j]))*(180/math.pi)
                if Di_mat[i,j] < 0:
                    Di_mat[i,j] = -Di_mat[i,j]
    
    
    ###Step-2 Non-maximal Suppression:
    Gn = np.zeros((row,col))             
    for i in range(0,row):
        for j in range(0,col):
            if i-1 >= 0 and i+1 < row and j-1 >= 0 and j+1 < col:
                if Di_mat[i,j] in range(0,23) or Di_mat[i,j] >= 158:
                    if M[i,j] > M[i,j+1] and M[i,j] > M[i,j-1]:
                        Gn[i,j] = M[i,j]
                elif Di_mat[i,j] in range(23,68):
                    if M[i,j] > M[i-1,j+1] and M[i,j] > M[i+1,j-1]:
                        Gn[i,j] = M[i,j]
                elif Di_mat[i,j] in range(68,113):
                    if M[i,j] > M[i-1,j] and M[i,j] > M[i+1,j]:
                        Gn[i,j] = M[i,j]
                else:
                    if M[i,j] > M[i-1,j-1] and M[i,j] > M[i+1,j+1]:
                        Gn[i,j] = M[i,j]
                        
    Gn = (Gn/np.max(M))*255 
    
    ##Step-3 Hysterisis Thresholding:
    Th = 200
    Tl = 100
    Gnh = np.zeros((row,col)) #For true edges
    Gnl = np.zeros((row,col)) #For weak edges
    for i in range(0,row):
        for j in range(0,col):
            if Gn[i,j] > Th:
                Gnh[i,j] = Gn[i,j]
            if Gn[i,j] > Tl:
                Gnl[i,j] = Gn[i,j]
        
    ##Step-4 Edge linking:
    Gnl2 = np.zeros((row,col))
    for i in range(0,row):
        for j in range(0,col):
            if i-1 >= 0 and i+1 < row and j-1 >= 0 and j+1 < col:
                neigh_8 = [Gnl[i-1,j-1], Gnl[i-1,j], Gnl[i-1,j+1], Gnl[i,j-1], Gnl[i,j+1], Gnl[i+1,j-1], Gnl[i+1,j], Gnl[i+1,j+1]]
                
                if Gnh[i,j] in neigh_8:
                    Gnl2[i,j] = Gnl[i,j]
                    
    Ie = Gnl2 + Gnh #Final Edge Map
    
    cv.imwrite('canny_edge_output.jpg', Ie.astype('uint8')) #Saving the output
    
    cv.imshow('Edge map',Ie.astype('uint8'))
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    return Ie.astype('uint8')


