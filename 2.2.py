import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\LENOVO\PycharmProjects\WelcomeScreen\gull-7539615_1280.jpg")

# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Displaying image using plt.imshow() method
plt.imshow(RGB_img)

# Hold the window
plt.waitforbuttonpress()

# Close all plots
plt.close('all')