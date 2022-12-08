# -*- coding: utf-8 -*-
# Copyright (C) 6/12/2022 16:27 PM, Inc. All Rights Reserved
# @Author  :Boyu_Zhang(Bob)
# @Software:Visual Studio Code
# @Email   :Boyuzhang215@gmail.com

# 范数对检测结果的影响

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("e:/python/Cambridge_12B_BoyuZhang/origin.png")
test1 = cv2.Canny(img, 000, 50,L2gradient=True)
test2 = cv2.Canny(img, 000, 100,L2gradient=True)
test3 = cv2.Canny(img, 000, 150,L2gradient=True)
test4 = cv2.Canny(img, 000, 200,L2gradient=True)
test5 = cv2.Canny(img, 000, 50,L2gradient=False)
test6 = cv2.Canny(img, 000, 100,L2gradient=False)
test7 = cv2.Canny(img, 000, 150,L2gradient=False)
test8 = cv2.Canny(img, 000, 200,L2gradient=False)


plt.subplot(3,4,9);plt.imshow(img,cmap = 'gray')
plt.title('Original'); plt.xticks([]); plt.yticks([])

plt.subplot(3,4,1);plt.imshow(test1,cmap = 'gray')
plt.title('0-50 L2gradient=True'); plt.xticks([]); plt.yticks([])
plt.subplot(3,4,2);plt.imshow(test2,cmap = 'gray')
plt.title('0-100 L2gradient=True'); plt.xticks([]); plt.yticks([])
plt.subplot(3,4,3);plt.imshow(test3,cmap = 'gray')
plt.title('0-150 L2gradient=True'); plt.xticks([]); plt.yticks([])
plt.subplot(3,4,4);plt.imshow(test4,cmap = 'gray')
plt.title('0-200 L2gradient=True'); plt.xticks([]); plt.yticks([])

plt.subplot(3,4,5);plt.imshow(test5,cmap = 'gray')
plt.title('0-50 L2gradient=False'); plt.xticks([]); plt.yticks([])
plt.subplot(3,4,6);plt.imshow(test6,cmap = 'gray')
plt.title('0-100 L2gradient=False'); plt.xticks([]); plt.yticks([])
plt.subplot(3,4,7);plt.imshow(test7,cmap = 'gray')
plt.title('0-150 L2gradient=False'); plt.xticks([]); plt.yticks([])
plt.subplot(3,4,8);plt.imshow(test8,cmap = 'gray')
plt.title('0-200 L2gradient=False'); plt.xticks([]); plt.yticks([])

plt.show()