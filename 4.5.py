import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('gull-7539615_1280.jpg')
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
filtered_image = cv2.medianBlur(image, 11)
cv2.imwrite('Median_Blur.jpg', filtered_image)
plt.subplot(1, 2, 2)
plt.title("Median Blur")
plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()