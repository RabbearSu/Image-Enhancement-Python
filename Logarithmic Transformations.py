import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\Users\\rabbear\\Desktop\\sky.jpg'

img = cv2.imread(path)

c=1.55
img_trans = c * np.log(1 + img /255)

plt.imshow(img_trans)
plt.show()
