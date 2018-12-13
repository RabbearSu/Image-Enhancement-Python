import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\Users\\rabbear\\Desktop\\sky.jpg'

img = cv2.imread(path)

#设置阈值函数为大于200设为255，小于200为0

img[img<210] = 0

plt.imshow(img)
plt.show()
