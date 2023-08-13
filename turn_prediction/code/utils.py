import numpy as np
import cv2
import matplotlib.pyplot as plt

def hist_eq(frame):
    image = np.asarray(frame)

    flat = image.flatten()
    histogram = get_histogram(flat, 256)
    cum_sum = get_cum_sum(histogram)
    cdf = get_cdf(cum_sum)

    cdf = cdf * 255
    cdf = cdf.astype('uint8')

    new_image = cdf[flat]
    new_image = np.reshape(new_image, image.shape)
    
    return new_image

def get_histogram(image, bins):
    histogram = np.zeros(bins)
    for pixel in image:
        histogram[pixel] += 1
    
    return histogram

def get_cum_sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
        array[i] = sum
    return array

def get_cdf(cum_sum):
    nr = (cum_sum - cum_sum.min())
    dr = cum_sum.max() - cum_sum.min()
    cdf = nr / dr
    return cdf

def adaptive_hist_eq(frame):  
    height = frame.shape[0]
    width = frame.shape[1]

    height_cutoff = height // 2
    width_cutoff = width // 4

    top_part = frame[:height_cutoff, :]
    bottom_part = frame[height_cutoff:, :]

    first_part = top_part[:, :width_cutoff]
    first_part = hist_eq(first_part)

    second_part = top_part[:, width_cutoff : width_cutoff * 2]
    second_part = hist_eq(second_part)

    third_part = top_part[:, width_cutoff * 2 : width_cutoff * 3]
    third_part = hist_eq(third_part)
    
    fourth_part = top_part[:, width_cutoff * 3 : width_cutoff * 4]
    fourth_part = hist_eq(fourth_part)
    
    fifth_part = bottom_part[:, :width_cutoff]
    fifth_part = hist_eq(fifth_part)
    
    sixth_part = bottom_part[:, width_cutoff : width_cutoff * 2]
    sixth_part = hist_eq(sixth_part)
    
    seventh_part = bottom_part[:, width_cutoff * 2 : width_cutoff * 3]
    seventh_part = hist_eq(seventh_part)
    
    eigth_part = bottom_part[:, width_cutoff * 3 : width_cutoff * 4]
    eigth_part = hist_eq(eigth_part)

    top = cv2.hconcat([first_part, second_part, third_part, fourth_part])
    bottom = cv2.hconcat([fifth_part, sixth_part, seventh_part, eigth_part])

    return cv2.vconcat([top, bottom])

def region(frame, points):
    mask = np.zeros_like(frame)
    cv2.fillPoly(mask, points, 255)
    img = cv2.bitwise_and(frame, mask)
    return img