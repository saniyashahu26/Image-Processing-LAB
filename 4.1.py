import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('gull-7539615_1280.jpg')
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
brightness = 10
contrast = 2.3
image2 = cv2.addWeighted(image,contrast,np.zeros(image.shape, image.dtype),0,brightness)
cv2.imwrite('modified_image.jpg', image2)
plt.subplot(1, 2, 2)
plt.title("Brightness & Contrast")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()