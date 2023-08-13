import numpy as np
import cv2

def optimal_cut():

    return []

# function that uses watershedding to find bright points and returns as lights
def light_roi(img):
    # Image Manipulation
    img = optimal_cut(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    th = img.max() / 4
    k = np.ones((9, 9), dtype=np.uint8)
    morph = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, k)
    _, thresh = cv2.threshold(morph, th, 255, cv2.THRESH_BINARY)

    # Watershed
    dist_transform = cv2.distanceTransform(np.uint8(thresh), cv2.DIST_L1, 3)
    _, markers = cv2.connectedComponents(np.uint8(dist_transform))
    markers += 1
    watershed_image = cv2.watershed(img, markers)
    max_size = 200
    values, counts = np.unique(watershed_image, return_counts=True)
    segment_indices = np.where(counts <= max_size)
    markers = values[segment_indices]
    coordinates = []
    for marker in markers:
        y_coordinates, x_coordinates = np.where(watershed_image == marker)
        coordinates.append((int(np.median(x_coordinates)), int(np.median(y_coordinates))))

    return coordinates
