import cv2
import numpy as np


# Image path
image_path = r"C:\Users\LENOVO\PycharmProjects\WelcomeScreen\images.jfif"


# Read image in grayscale
image = cv2.imread(
    image_path,
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    raise FileNotFoundError(
        "Image not found. Check the path."
    )


# Convert image to binary
_, binary = cv2.threshold(
    image,
    127,
    255,
    cv2.THRESH_BINARY
)


# Create morphological kernel
kernel_size = (5, 5)

kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    kernel_size
)


# Apply morphological operations
morph_ops = {
    "Erosion": cv2.erode(
        binary,
        kernel,
        iterations=1
    ),

    "Dilation": cv2.dilate(
        binary,
        kernel,
        iterations=1
    ),

    "Opening": cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel
    ),

    "Closing": cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        kernel
    )
}


# Function to calculate object areas
def calculate_object_areas(binary_img):
    contours, _ = cv2.findContours(
        binary_img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    areas = [
        cv2.contourArea(c)
        for c in contours
    ]

    return areas, contours


# Process each morphological operation
for op_name, op_img in morph_ops.items():

    areas, contours = calculate_object_areas(op_img)

    print(
        f"{op_name}: Number of objects = {len(areas)}, "
        f"Areas = {areas}"
    )

    # Convert grayscale image to BGR
    contoured_img = cv2.cvtColor(
        op_img,
        cv2.COLOR_GRAY2BGR
    )

    # Draw contours
    cv2.drawContours(
        contoured_img,
        contours,
        -1,
        (0, 0, 255),
        2
    )

    # Display result
    cv2.imshow(
        f"{op_name} with Contours",
        contoured_img
    )


# Display original binary image
cv2.imshow(
    "Original Binary",
    binary
)


# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()