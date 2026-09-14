import cv2
image = cv2.imread('gull-7539615_1280.jpg')
kernel_size = 5
filtered_image = cv2.medianBlur(image, kernel_size)
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image (Median Blur)', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()