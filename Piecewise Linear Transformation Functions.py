import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
path = 'C:\\Users\\rabbear\\Desktop\\sky.jpg'

img = cv2.imread(path)

img = img/255
img = 0.5 * img
img[img<(50/255)] = 2 * img[img<(50/255)]
img[img>(100/255)] = 2 * img[img>(100/255)]


plt.imshow(img)
plt.show()