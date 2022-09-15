import cv2

# Reading image file
img = cv2.imread('images/Python.png')
 
# Applying NumPy scalar multiplication on image
fimg = img * 1.5
 
# Saving the output image
cv2.imwrite('images/output_multiplication_Numpy.jpg', fimg)