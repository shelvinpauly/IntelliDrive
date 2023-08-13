import numpy as np
import cv2

# function finds red, yellow, and whit eblobs and returns as sign coords with size
def sign_roi(img):
    width = int(img.shape[1])
    height = int(img.shape[0])

    bottom_mask_height = 5 * height // 12
    bottom_slope = -bottom_mask_height / (width / 2)

    top_mask_height = 7 * height // 12
    top_slope = (height - top_mask_height) / (width / 2)

    region_mask = [
        [0 if height - y <= int(bottom_mask_height + bottom_slope * abs(x - width // 2)) or height - y >= int(
            top_mask_height + top_slope * abs(x - width // 2)) else 1 for x in range(0, width)] for y in
        range(0, height)]
    region_mask = (np.array(region_mask)).astype(np.uint8)


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 0, 200])
    upper_red = np.array([75, 75, 255])
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    lower_white = np.array([0, 0, 230])
    upper_white = np.array([0, 25, 255])

    red_mask = cv2.inRange(img, lower_red, upper_red)
    yellow_mask = cv2.inRange(img, lower_yellow, upper_yellow)
    white_mask = cv2.inRange(img, lower_white, upper_white)

    masks = [red_mask, yellow_mask, white_mask]

    detector = cv2.SimpleBlobDetector()
    blobs = [detector.detect(mask) for mask in masks]

    points = []
    for color in blobs:
        for blob in color:
            point = [blob.pt[0], blob.pt[1], blob.size]
            points.append(point)

    return points


