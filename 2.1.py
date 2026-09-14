import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Users\LENOVO\PycharmProjects\WelcomeScreen\gull-7539615_1280.jpg')
plt.imshow(img)
plt.waitforbuttonpress()
plt.close('all')