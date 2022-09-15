import cv2

# Reading image files
img1 = cv2.imread('images/Python.png')
img2 = cv2.imread('images/Tensorflow.png')
 
# Applying OpenCV subtraction on images
fimg = cv2.subtract(img1, img2)
 
# Saving the output image
cv2.imwrite('images/output_subtraction.jpg', fimg)