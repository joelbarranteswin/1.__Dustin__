# importing cv2 module
import cv2

# Image path
image_path = './forest.jpg'

# Using cv2.imread() method to read the image
img = cv2.imread(image_path)

# New image Filename
filename = 'saved_new.jpg'

# Using cv2.imwrite() method saving the image
cv2.imwrite(filename, img)

print('The image is saved Successfully')
