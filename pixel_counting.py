import cv2
import numpy as np

img = cv2.imread("C:\\Users\\User\\Desktop\\website\\public\\img\\2.PNG", 9)
n_black_pix = np.sum(img == 0)
n_white_pix = np.sum(img == 255)
print('Number of black pixels:', n_black_pix)
a = n_black_pix/(n_black_pix + n_white_pix)
print(a)
b = (1-a)*100
print("The Effective Density of Fog is",b)
cv2.imshow("a", img)
