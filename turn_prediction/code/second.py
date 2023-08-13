from utils import *

vid_capture = cv2.VideoCapture("/home/sln/catkin_ws/src/proj/input/whiteline.mp4")
ret, frame = vid_capture.read()
points = np.array([[(350,355),(590,355),(950,540),(40,540)]])

vid  = cv2.VideoWriter('second.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (960,540))
i = 0
while ret:
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    temp = region(gray, points)
    _, thresh = cv2.threshold(temp, 150, 255, cv2.THRESH_BINARY)
    new = region(thresh, points)
    edge = cv2.Canny(new, 10, 150)

    pts_1 = np.float32([[(350, 355), (590, 355), (40, 540), (950, 540)]])
    pts_2 = np.float32([[(0, 0), (480, 0), (0, 600), (480, 600)]])
    bird = cv2.getPerspectiveTransform(pts_1, pts_2)
    bird = cv2.warpPerspective(edge, bird, (480, 600), flags = cv2.INTER_LANCZOS4)
    
    histogram = np.sum(bird, axis=0)
    mid = int(histogram.shape[0] / 2)
    left = np.sum(histogram[:mid])
    right = np.sum(histogram[mid:])
    if left > right:
        left = (0, 255, 0)
        right = (0,0,255)
    else:
        left = (0, 0, 255)
        right = (0, 255, 0)
    left_lines = cv2.HoughLinesP(edge[:, :480], 2, np.pi / 180, 100, np.array([]), minLineLength = 100, maxLineGap = 250)
    right_lines = cv2.HoughLinesP(edge[:, 480:], 2, np.pi / 180, 100, np.array([]), minLineLength=7, maxLineGap=50)
    
    lines = np.zeros_like(frame)
    if left_lines is not None:
        for line in left_lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1),(x2, y2), left, 5)
    img = cv2.addWeighted(frame, 0.75, lines, 1, 1)
    if right_lines is not None:
        for line in right_lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1 + 480, y1), (x2 + 480, y2), right, 5)
    final = cv2.addWeighted(frame, 0.75, img, 1, 1)

    #print(final.shape)
    # final = cv2.resize(final, (1280, 720))
    vid.write(final)
    ret, frame = vid_capture.read()


cv2.waitKey(0)
cv2.destroyAllWindows()
vid.release()
vid_capture.release()