# “TURTLE海龟画图”

一些实现过程 $\downarrow$

---

# 依赖
详见：'requirements.txt'. 

### 依赖安装:
```
 "pip install -r requirements.txt"
```

---

# 原理
## OpenCV-Python：
主要使用 $OpenCV$ 中的 $cv2.Canny()$ 边缘检测工具  
在进行边缘之前需要对图像进行模糊处理‘
### Canny()主要实现思想：
1. 使用高斯模糊，去除噪音点($e.g.$ $cv2.blur()$，$cv2.GaussianBlur$)
2. 灰度转换（$cv2.cvtColor$）
3. 使用sobel算子，计算出每个点的梯度大小和梯度方向
4. 使用非极大值抑制(只有最大的保留)，消除边缘检测带来的杂散效应
5. 应用双阈值，来确定真实和潜在的边缘
6. 通过抑制弱边缘来完成最终的边缘检测

### 边缘检测
```
edge = cv2.Canny(image,threshold1,threshold2,edges,apertureSize,L2gradient) 
```
> ### 参数含义如下:
> 1. image: 要处理的图像  
> 2. threshold1: 阈值1（min）  
> 3. threshold2: 阈值2（max），使用此参数进行明显的边缘检测  
> 4. edges: 图像边缘信息  
> 5. apertureSize: sobel算子（卷积核）大小  （通常取值在3-7之间的奇数）
> 6. L2gradient: 布尔值。  
>       True: 使用更精确的L2范数进行计算（即两个方向的导数的平方和再开方）  
>       False: 使用L1范数（直接将两个方向导数的绝对值相加）  
> $Edge\_Fraduebt(G)=\sqrt{G^{2}_{x}+G^{2}_{y}}$ (True)  
> $Edge\_Fraduebt(G)=|G_{x}|+|G_{y}|$ (False)
>
> 注意: 阈值小=细节多，算子大=细节多，范数为假=细节多，反之亦然。


---
---
# 测试
## 1.阈值对检测结果的影响
测试代码
```
test1.py
```
![Alt text](https://raw.githubusercontent.com/zby215/draw-image-by-using-OpenCV-and-turtle/main/Image/%E9%98%88%E5%80%BC%E5%AF%B9%E6%A3%80%E6%B5%8B%E7%BB%93%E6%9E%9C%E7%9A%84%E5%BD%B1%E5%93%8D.png)

## 2.sobel算子对检测结果的影响
测试代码
```
test2.py
```
![Alt text](https://raw.githubusercontent.com/zby215/draw-image-by-using-OpenCV-and-turtle/main/Image/sobel%E7%AE%97%E5%AD%90%E5%AF%B9%E6%A3%80%E6%B5%8B%E7%BB%93%E6%9E%9C%E7%9A%84%E5%BD%B1%E5%93%8D.png)

## 3.范数对检测结果的影响
测试代码
```
test3.py
```
![Alt text](https://raw.githubusercontent.com/zby215/draw-image-by-using-OpenCV-and-turtle/main/Image/%E8%8C%83%E6%95%B0%E5%AF%B9%E6%A3%80%E6%B5%8B%E7%BB%93%E6%9E%9C%E7%9A%84%E5%BD%B1%E5%93%8D.png)

## 结论
> 阈值为0，200 ; 卷积核大小为3 ; L2范数为1 时，效果最好

---

# 代码
> 导入需要的第三方库&变量声明
```python
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
```

> 读取图片
```python
img = cv2.imread("Cambridge_12B_BoyuZhang/Image/origin.png")
```

> 图片处理（图片$\rightarrow$坐标矩阵）
```python
# image processing
image = cv2.Canny(img, 000, 200, apertureSize=3, L2gradient=True)

# get image size
image_x, image_y = image.shape[:2]

# resize and get coordinate file
points_set = cv2.resize(image, (int(image_y/2), int(image_x/2)),
                   interpolation=cv2.INTER_CUBIC)
points_set = numpy.rot90(points_set, k=-1)
```

> turtle 绘画
```python
turtle.setup(window_y, window_x)
turtle.pensize(4)
turtle.speed(0)
for y in range(0, len(points_set), 1):
    for x in range(0, len(points_set[y]), 2):
        if point[y][x] != 0:
            turtle.penup()
            turtle.goto(y-499, x-250)
            turtle.pendown()
            turtle.goto(y-499, x-250)
            turtle.penup()
```
> 导出为eps格式图片
```python
# export image with format eps
turtle.getcanvas().postscript(file="剑桥_12B_张搏禹1.eps")
turtle.done()
```

---
---
# 成品
## 原图
![Alt text](https://raw.githubusercontent.com/zby215/draw-image-by-using-OpenCV-and-turtle/main/Image/origin.png)
## turtle绘画
![Alt text](https://raw.githubusercontent.com/zby215/draw-image-by-using-OpenCV-and-turtle/main/Image/OUTPUT.png)
