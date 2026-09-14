import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('gull-7539615_1280.jpg')
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened = cv2.filter2D(image, -1, kernel)
plt.subplot(1, 2, 2)
plt.title("Sharpened")
plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()