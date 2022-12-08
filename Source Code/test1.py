# -*- coding: utf-8 -*-
# Copyright (C) 6/12/2022 15:44 PM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:Visual Studio Code
# @Email   :Boyuzhang215@gmail.com

# 阈值对检测结果的影响
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("e:/python/Cambridge_12B_BoyuZhang/origin.png")
test1 = cv2.Canny(img, 000, 50)
test2 = cv2.Canny(img, 000, 100)
test3 = cv2.Canny(img, 000, 150)
test4 = cv2.Canny(img, 000, 200)
test5 = cv2.Canny(img, 50, 100)
test6 = cv2.Canny(img, 50, 150)
test7 = cv2.Canny(img, 50, 200)
test8 = cv2.Canny(img, 100, 150)
test9 = cv2.Canny(img, 100, 200)
test10 = cv2.Canny(img, 150, 200)

plt.subplot(4,4,13);plt.imshow(img,cmap = 'gray')
plt.title('Original'); plt.xticks([]); plt.yticks([])

plt.subplot(4,4,1);plt.imshow(test1,cmap = 'gray')
plt.title('0-50'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,2);plt.imshow(test2,cmap = 'gray')
plt.title('0-100'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,3);plt.imshow(test3,cmap = 'gray')
plt.title('0-150'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,4);plt.imshow(test4,cmap = 'gray')
plt.title('0-200'); plt.xticks([]); plt.yticks([])

plt.subplot(4,4,6);plt.imshow(test5,cmap = 'gray')
plt.title('50-100'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,7);plt.imshow(test6,cmap = 'gray')
plt.title('50-150'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,8);plt.imshow(test7,cmap = 'gray')
plt.title('50-200'); plt.xticks([]); plt.yticks([])

plt.subplot(4,4,11);plt.imshow(test8,cmap = 'gray')
plt.title('100-150'); plt.xticks([]); plt.yticks([])
plt.subplot(4,4,12);plt.imshow(test9,cmap = 'gray')
plt.title('100-200'); plt.xticks([]); plt.yticks([])

plt.subplot(4,4,16);plt.imshow(test10,cmap = 'gray')
plt.title('150-200'); plt.xticks([]); plt.yticks([])
plt.show()