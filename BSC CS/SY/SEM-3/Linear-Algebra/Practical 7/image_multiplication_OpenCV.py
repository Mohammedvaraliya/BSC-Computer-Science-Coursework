import cv2

# Reading image file
img = cv2.imread('images/Python.png')
 
# Applying OpenCV scalar multiplication on image
fimg = cv2.multiply(img, 1.5)
 
# Saving the output image
cv2.imwrite('images/output_multiplication_OpenCV.jpg', fimg)