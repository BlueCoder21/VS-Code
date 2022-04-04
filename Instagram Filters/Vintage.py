from warnings import filterwarnings
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("fruit.jpeg")
rows,cols= img.shape[:2]
#cret gassi filt
kernel_x = cv2.getGaussianKernel(cols,200)
kernel_y = cv2.getGaussianKernel(rows,200)
kernel = kernel_y * kernel_x.T
filter = 255 * kernel / np.linalg.norm(kernel)
vintage = np.copy(img)
for i in range(3):
    vintage[:,:,i] = vintage[:,:,i] * filter
plt.imshow(vintage)
plt.show()