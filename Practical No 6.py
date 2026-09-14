import cv2
import numpy as np

damaged_img = cv2.imread("gull-7539615_1280.jpg")
height, width = damaged_img.shape[0], damaged_img.shape[1]

mask = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        if damaged_img[i, j].sum() > 0:
            mask[i, j] = [0, 0, 0]
        else:
            mask[i, j] = [255, 255, 255]

mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gull-7539615_1280.jpg", mask_gray)
restored_telea = cv2.inpaint(
    damaged_img,
    mask_gray,
    3,
    cv2.INPAINT_TELEA
)
img = cv2.imread("gull-7539615_1280.jpg")
mask_predefined = cv2.imread("gull-7539615_1280.jpg", 0)
restored_ns = cv2.inpaint(
    img,
    mask_predefined,
    3,
    cv2.INPAINT_NS
)

cv2.imwrite("restored_telea.png", restored_telea)
cv2.imwrite("restored_ns.png", restored_ns)

cv2.imshow("Original Damaged Image", damaged_img)
cv2.imshow("Generated Mask", mask_gray)
cv2.imshow("Restored (Telea)", restored_telea)
cv2.imshow("Predefined Mask", mask_predefined)
cv2.imshow("Restored (Navier-Stokes)", restored_ns)
cv2.waitKey(0)
cv2.destroyAllWindows()