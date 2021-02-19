"""
Gestione di metodi e librerie di supporto.
"""
import os
import numpy as np 
import matplotlib.pyplot as pyplot
from cv2 import cv2
from PIL import Image
import sys
import glob

BLUE = [255, 0, 0]
GREEN = [0, 255, 0]
RED = [0, 0, 255]

COLORS = [BLUE, GREEN, RED]

def drawPoints(points, img, save_path, color):
    
    for x, y in points:
        x_rounded = int(round(x))
        y_rounded = int(round(y))

        cv2.circle(img, (x_rounded, y_rounded),
            radius=2,
            color=COLORS[2],
            thickness=3,
            lineType=cv2.LINE_AA)
    
    cv2.imwrite(save_path, img)

def drawLines(points, img1, img2, save_path, color):

    width = img1.shape[1]

    img_merge = np.hstack((img1, img2))

    for x1, y1, x2, y2 in points:
        x1_rounded = int(round(x1))
        y1_rounded = int(round(y1))
        x2_rounded = int(round(x2) + width)
        y2_rounded = int(round(y2))

        cv2.line(img_merge, (x1_rounded, y1_rounded), (x2_rounded, y2_rounded),
            color=COLORS[color],
            thickness=2)
        
        cv2.imwrite(save_path, img_merge)

def renameImages(main_path):
    """
    La funzione 'renameImages' rinomina le immagini della cartella input.
    """
    i = 1
    for fileName in os.listdir(main_path + '\\input\\'):
        os.rename(main_path + '\\input\\' + fileName, main_path + '\\input\\' + str(i) + '.tif')
        i = i + 1

def loadImages(main_path):
    """
    La funzione 'loadImages' carica tutte le immagini contenute nel percorso selezionato
    """
    images_number = len(glob.glob1(main_path + '\\input\\', '*.tif')) + 1

    renameImages(main_path)

    images_name = []
    images = []

    for i in range(1, images_number):
        images_name.append(str(i) + '.tif')

    for i in range(0, images_number - 1):
        main_path + '\\input\\' + images_name[i]
        image = cv2.imread(main_path + '\\input\\' + images_name[i])
        images.append(image)
    return images, images_name, images_number