import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\Users\\rabbear\\Desktop\\sky.jpg'

img = cv2.imread(path)

c=1
r=0.4

img_gamma = c * np.power(img/255, r)

plt.imshow(img_gamma)
plt.show()