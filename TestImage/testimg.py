import cv2
import numpy as np


def identify_image(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create an image with only the edges of the original image
    edges = cv2.Canny(gray_image, 100, 200)

    # Count the number of lines in the edge image
    lines = cv2.HoughLinesP(edges, 1, np.pi/180,
                            threshold=100, minLineLength=100, maxLineGap=10)
    line_count = len(lines)

    # Compare the number of lines to a threshold to decide whether the image is a drawing or photograph
    if line_count > 50:
        return "drawing."
    else:
        return "photograph"
