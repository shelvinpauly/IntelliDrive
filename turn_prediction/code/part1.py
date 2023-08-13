from utils import *

vid  = cv2.VideoWriter('part_1.avi', cv2.VideoWriter_fourcc(*'XVID'), 2, (1224, 370))

frame = cv2.imread("input/data1/0000000000.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000001.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000002.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000003.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000004.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000005.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000006.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000007.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000008.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000009.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000010.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000011.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000012.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000013.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000014.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000015.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000016.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000017.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000018.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000019.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000020.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)

frame = cv2.imread("input/data1/0000000021.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000022.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000023.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

frame = cv2.imread("input/data1/0000000024.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
new_image = hist_eq(gray)
vid.write(new_image)

# cv2.imshow('Histogram Equalization', new_image)
# cv2.waitKey()
# cv2.destroyAllWindows()
#cv2.imwrite('part1.jpg', new_image)


vid.release()