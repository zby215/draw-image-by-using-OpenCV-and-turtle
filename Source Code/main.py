# -*- coding: utf-8 -*-
# Copyright (C) 7/12/2022 11:24 AM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:Visual Studio Code
# @Email   :Boyuzhang215@gmail.com
import cv2
import turtle
import numpy
import sys

# window size
window_x = 1080
window_y = 1920

# image size
image_x = 0
image_y = 0

# image reading
img = cv2.imread("Cambridge_12B_BoyuZhang/Image/origin.png")

# show original image（No effect to program）
# cv2.imshow("origin",img)

# image processing
image = cv2.Canny(img, 000, 200, apertureSize=3, L2gradient=True)

# get image size
image_x, image_y = image.shape[:2]

# resize and get coordinate file
points_set = cv2.resize(image, (int(image_y/2), int(image_x/2)),
                   interpolation=cv2.INTER_CUBIC)
points_set = numpy.rot90(points_set, k=-1)


# turtle drawing start
turtle.setup(window_y, window_x)
turtle.pensize(4)
turtle.speed(0)
for y in range(0, len(points_set), 1):
    for x in range(0, len(points_set[y]), 2):
        if points_set[y][x] != 0:
            # get coordinate of pen(No effect to program)
            # xp, yp = turtle.pos()
            # print(xp, yp,end="\t")
            # print(y, x)
            turtle.penup()
            turtle.goto(y-499, x-250)
            turtle.pendown()
            turtle.goto(y-499, x-250)
            turtle.penup()

# export image with format eps
turtle.getcanvas().postscript(file="剑桥_12B_张搏禹1.eps")
turtle.done()

# exit program
sys.exit()
