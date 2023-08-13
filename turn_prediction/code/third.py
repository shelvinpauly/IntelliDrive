import numpy as np
import cv2

vid_capture = cv2.VideoCapture('input/challenge.mp4')
ret, frame = vid_capture.read()
vid  = cv2.VideoWriter('third.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (1280,720))

#print(frame.shape)

while ret:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    thresh_1 = np.zeros((thresh.shape[0], thresh.shape[1], 3), dtype = 'uint8')
    thresh_1[:, :, 0] = thresh
    thresh_1[:, :, 1] = thresh
    thresh_1[:, :, 2] = thresh

    temp_1 = np.zeros((600, 400, 3), dtype = 'uint8')
    points_1 = np.array([[100, 700], [500, 460], [750, 460],[1300, 700]])
    points_2 = np.array([[0, temp_1.shape[0]], [0, 0], [temp_1.shape[1], 0], [temp_1.shape[1], temp_1.shape[0]]])
    h,_ = cv2.findHomography(points_1, points_2)
    bird = cv2.warpPerspective(frame, h, (temp_1.shape[1], temp_1.shape[0]))
    # cv2.imshow("view",bird)
    # cv2.waitKey(0)
    
    gray = cv2.cvtColor(bird, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    thresh_2 = np.zeros((thresh.shape[0], thresh.shape[1], 3), dtype = 'uint8')
    thresh_2[:, :, 0] = thresh
    thresh_2[:, :, 1] = thresh
    thresh_2[:, :, 2] = thresh
    lane = thresh_2.copy()

    # cv2.imshow("view",lane)
    # cv2.waitKey(0)

    empty = np.zeros_like(bird)

    #Lane Detection and prediction
    low = np.array([10, 100, 160])  
    high = np.array([35, 255, 255])
    hsv = cv2.cvtColor(bird, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low, high)
    yellow = np.where(mask != 0)

    coefficient = np.polyfit(yellow[0][:], yellow[1][:], 2)
    y = np.linspace(0, bird.shape[0], 40)
    x = np.polyval(coefficient, y)

    yellow_radius = np.abs(float((1 + (2 * coefficient[0] * y[20] + coefficient[1]) ** 2) ** (3.0/2.0)) / float(2 * coefficient[0]))
    yellow_points = (np.asarray([x, y]).T).astype(np.int32)
    cv2.polylines(empty, [yellow_points], False, (0 , 0, 255), thickness = 5)
    cv2.polylines(lane, [yellow_points], False, (0, 0, 255), thickness = 2)

    for points in yellow_points:
        points = tuple(points)
        if points[1] == 600:
            continue
        if mask[points[1], points[0]] == 0:
            continue
        cv2.circle(lane, points, 5, (0, 255, 255), thickness = 2)

    white = cv2.cvtColor(bird, cv2.COLOR_BGR2GRAY)
    _, white = cv2.threshold(white, 225, 255, cv2.THRESH_BINARY)
    white_points = np.where(white != 0)

    coefficient = np.polyfit(white_points[0][:], white_points[1][:], 2)
    y = np.linspace(0, bird.shape[0], 40)
    x = np.polyval(coefficient, y)

    white_radius = np.abs(float((1 + (2 * coefficient[0]* y[20] + coefficient[1]) **2 ) ** (3.0/2.0)) / float(2 * coefficient[0]))
    white_lane_points = (np.asarray([x, y]).T).astype(np.int32)

    cv2.polylines(empty, [white_lane_points], False, (0,0,255), thickness = 5)
    cv2.polylines(lane, [white_lane_points], False, (0,0,255), thickness = 2)

    for points in white_lane_points:
        points = tuple(points)
        if points[1] == 600:
            continue
        if white[points[1],points[0]] == 0:
            continue
        cv2.circle(lane, points, 5, (0, 255, 255),thickness = 2)

    #Calculate turn
    radius = round((yellow_radius + white_radius) / 2.0, 2)

    yellow_points = np.flipud(yellow_points)
    points = np.concatenate((white_lane_points, yellow_points))
    cv2.fillPoly(empty, [points], color = [0, 0, 255])

    h,_ = cv2.findHomography(points_1, points_2)
    temp = cv2.warpPerspective(empty, h, (frame.shape[1], frame.shape[0]))
    final = cv2.add(frame, temp)
    final = cv2.resize(final, (int(frame.shape[1] * 0.7), int(frame.shape[0] * 0.25) + int(frame.shape[0] * 0.45)))

    if coefficient[0] < 0:
        cv2.putText(final, 'Left Turn', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255) , 2)
    elif coefficient[0] > 0:
        cv2.putText(final, 'Right Turn', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255) , 2)
    else:
        cv2.putText(final, 'Straight', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255) , 2)


    vid_1 = np.concatenate((frame, thresh_1), axis = 1)
    vid_1 = cv2.resize(vid_1, (int(frame.shape[1] * 0.25), int(frame.shape[0] * 0.25)))
    cv2.putText(vid_1, '(1)', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0) , 2)
    cv2.putText(vid_1, '(2)', (180, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0) , 2)
    vid_2 = np.concatenate((thresh_2, lane), axis = 1)
    vid_2 = cv2.resize(vid_2, (int(frame.shape[1] * 0.25), int(frame.shape[0] * 0.45)))
    cv2.putText(vid_2, '(3)', (30, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0) , 2)
    cv2.putText(vid_2, '(4)', (180, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0) , 2)
    vid_3 = np.concatenate((vid_1, vid_2), axis = 0)
    vid_4 = np.concatenate((final, vid_3), axis = 1)
    vid_5 = np.zeros([int(frame.shape[0] * 0.10), int(frame.shape[1] * 0.70) + int(frame.shape[1] * 0.25), 3], dtype = np.uint8)
    vid_5.fill(255)
    cv2.putText(vid_5, '(1): Undistorted image, (2): Detected white and yellow lane markings, (3): Warped image, (4): Detected points and curve fitting', (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(vid_5, 'Turn Radius:' + " " + str(radius), (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    vid_6 = np.concatenate((vid_4, vid_5), axis = 0)
    vid_6 = cv2.resize(vid_6, (1280, 720))
    # cv2.imshow('video', video6)
    #print(video6.shape)
    vid.write(vid_6)
    ret, frame = vid_capture.read()

vid.release()
vid_capture.release()
