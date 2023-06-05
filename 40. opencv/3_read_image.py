import cv2

path = 'C:/Users/joel_/Documents/GitHub/Python_beyond_practices/40. opencv/src/deep_image.png'

# Using cv2.imread() method
image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

# Displaying the image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destoryAllWindows()
