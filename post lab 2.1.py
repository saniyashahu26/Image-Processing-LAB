import cv2

# Read the image
image = cv2.imread("images.jfif")

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Split the image into B, G, R channels
    B, G, R = cv2.split(image)

    # Show the original image
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    # Show blue channel
    cv2.imshow("Blue", B)
    cv2.waitKey(0)

    # Show green channel
    cv2.imshow("Green", G)
    cv2.waitKey(0)

    # Show red channel
    cv2.imshow("Red", R)
    cv2.waitKey(0)

    cv2.destroyAllWindows()