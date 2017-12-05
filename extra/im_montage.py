import cv2
import numpy as np
import glob

file_path = "/home/kushal/college_acads/sem_8/test_latex_word/thesis/fig/woodland/model/*.jpg"
files =  sorted(glob.glob(file_path))

im = cv2.imread(files[0])
print im.shape
ratio = 0.07
w = int(ratio*im.shape[1])
h = int(ratio*im.shape[0])
im = cv2.resize(im,  (int(w) ,int(h)))
print im.shape
cv2.imshow("im", im)
cv2.waitKey()
cv2.destroyAllWindows()

grid = (11, 4)
rows = grid[0] * h ; cols = grid[1]*w; ch=3
montage = np.zeros((rows, cols, ch), np.uint8)
print montage.shape

start = (0, 0)
for i in range(grid[0]):
	for j in range(grid[1]):
		if (i*4 + j) > 41:
			break
		start_x = w * j
		start_y = h*i
		print i*4 + j
		x = cv2.resize(cv2.imread(files[i*4 + j]), (w, h))
		montage[start_y : start_y + h , start_x : start_x + w , :] = x

cv2.imshow("montage", montage)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("montage_" + file_path.split("/")[-3]+".png", montage)