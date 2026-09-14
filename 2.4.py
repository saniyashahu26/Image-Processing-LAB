import cv2
image_path = (r'C:\Users\LENOVO\PycharmProjects\WelcomeScreen\gull-7539615_1280.jpg')
directory = r'C:\Users\LENOVO\PycharmProjects\WelcomeScreen'
import os
image_path = r'C:\Users\LENOVO\PycharmProjects\WelcomeScreen\gull-7539615_1280.jpg'
directory = r"C:\Users\LENOVO\PycharmProjects\WelcomeScreen"
img = cv2.imread(image_path)
os.chdir(directory)
print("Before saving image:")
print(os.listdir(directory))
filename = 'savedImage.jpg'
cv2.imwrite(filename, img)
print("After saving image:")
print(os.listdir(directory))
print('Successfully saved')