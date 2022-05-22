# Made my pdsatter
# Date: 5/22/2022

import cv2
import random

img = cv2.imread('assets/github.png', 1)

for i in range(img.shape[0]): # Makes rows 50 - 100 random colors
    for j in range(img.shape[1]): # img.shape[1] gets the width
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imwrite('assets/scrambled-github.png', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
