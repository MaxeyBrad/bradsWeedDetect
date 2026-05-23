# Test file for HSV
import cv2
import numpy

# Load image from disk
img = cv2.imread("images/leaf.jpeg")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Set bounds 
lower_green = numpy.array([35,40,40])
upper_green = numpy.array([85,255,255])

# Create mask
mask = cv2.inRange(hsv, lower_green, upper_green)

#Display
cv2.imshow("Test image",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
