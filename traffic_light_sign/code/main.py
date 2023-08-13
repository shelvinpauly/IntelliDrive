import numpy as np
import torch
import cv2
import light_detect
import traffic_sign_interest
import classifier

# main function for implementing the ROI classifier for traffic
def main():
    vid = cv2.VideoCapture('IMG_3631.mov')
    width = int(vid.get(3))
    height = int(vid.get(4))
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
    while True:
        stat, frame = vid.read()
        if not stat:
            break

        light_coords = light_detect.light_roi(frame)
        sign_coords = traffic_sign_interest.sign_roi(frame)

	# make regions for coordinates for lights and signs
        for light in light_coords:
            y, x = light
            if y < 20:
                y = 20
            if y > height-20:
                y = height-20
            if x < 20:
                x = 20
            if x > width-20:
                x = width-20

            frame[y-20:y+20, x-20:x+20] = classifier.classify(frame[y-20:y+20, x-20:x+20], False)

        for sign in sign_coords:
            y, x, w = sign
            if y < 20 + w:
                y = 20 + w
            if y > height-20 - w:
                y = height-20 - w
            if x < 20 + w:
                x = 20 + w
            if x > width-20 - w:
                x = width-20 - w

	# run functions on regions and return and replace section of image
            frame[y - 20-w:y + 20+w, x - 20-w:x + 20+w] = classifier.classify(frame[y - 20-w:y + 20+w, x - 20-w:x + 20+w], True)

	# output video
        out.write(frame)
    out.release()
