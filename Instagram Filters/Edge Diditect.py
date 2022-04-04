import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpeg")
edge_diditection = cv2.Canny(img,100,300)
plt.imshow(edge_diditection)
plt.show()