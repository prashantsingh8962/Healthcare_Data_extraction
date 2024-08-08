import cv2
import numpy as np


def preprocess_image(img):
    # Convert the PIL image to a NumPy array
    img_array = np.array(img)

    # Convert the image from RGB to grayscale
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Resize the image
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    # Apply adaptive thresholding
    processed_image = cv2.adaptiveThreshold(
        resized, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )

    return processed_image