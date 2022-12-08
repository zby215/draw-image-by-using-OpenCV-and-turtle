# -*- coding: utf-8 -*-
# Copyright (C) 6/12/2022 16:02 PM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:Visual Studio Code
# @Email   :Boyuzhang215@gmail.com

# sobel算子对检测结果的影响

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("e:/python/Cambridge_12B_BoyuZhang/origin.png")
test1 = cv2.Canny(img, 000, 50,apertureSize=3)
test2 = cv2.Canny(img, 000, 100,apertureSize=3)
test3 = cv2.Canny(img, 000, 150,apertureSize=3)
test4 = cv2.Canny(img, 000, 200,apertureSize=3)
test5 = cv2.Canny(img, 000, 50,apertureSize=5)
test6 = cv2.Canny(img, 000, 100,apertureSize=5)
test7 = cv2.Canny(img, 000, 150,apertureSize=5)
test8 = cv2.Canny(img, 000, 200,apertureSize=5)
test9 = cv2.Canny(img, 000, 50,apertureSize=7)
test10 = cv2.Canny(img, 000, 100,apertureSize=7)
test11 = cv2.Canny(img, 000, 150,apertureSize=7)
test12 = cv2.Canny(img, 000, 200,apertureSize=7)

plt.subplot(4,4,13);plt.imshow(img,cmap = 'gray')
plt.title('Original'); plt.xticks([]); plt.yticks([])

plt.subplot(4,4,1);plt.imshow(test1,cmap = 'gray')
plt.title('0-50 apertureSize=3'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,2);plt.imshow(test2,cmap = 'gray')
plt.title('0-100 apertureSize=3'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,3);plt.imshow(test3,cmap = 'gray')
plt.title('0-150 apertureSize=3'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,4);plt.imshow(test4,cmap = 'gray')
plt.title('0-200 apertureSize=3'); plt.xticks([]); plt.yticks([])

plt.subplot(4,4,5);plt.imshow(test5,cmap = 'gray')
plt.title('0-50 apertureSize=5'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,6);plt.imshow(test6,cmap = 'gray')
plt.title('0-100 apertureSize=5'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,7);plt.imshow(test7,cmap = 'gray')
plt.title('0-150 apertureSize=5'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,8);plt.imshow(test8,cmap = 'gray')
plt.title('0-200 apertureSize=5'); plt.xticks([]); plt.yticks([])

plt.subplot(4,4,9);plt.imshow(test9,cmap = 'gray')
plt.title('0-50 apertureSize=7'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,10);plt.imshow(test10,cmap = 'gray')
plt.title('0-100 apertureSize=7'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,11);plt.imshow(test11,cmap = 'gray')
plt.title('0-150 apertureSize=7'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,12);plt.imshow(test12,cmap = 'gray')
plt.title('0-200 apertureSize=7'); plt.xticks([]); plt.yticks([])

plt.show()