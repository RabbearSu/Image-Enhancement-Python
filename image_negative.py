import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\Users\\rabbear\\Desktop\\sky.jpg'

img = cv2.imread(path)

img_negative = 256 - img

plt.imshow(img)
plt.imshow(img_negative)
plt.show()
