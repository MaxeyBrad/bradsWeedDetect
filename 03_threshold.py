# Test file for Thresholding
import cv2
import numpy

# Load image from disk
img = cv2.imread("images/leaf.jpeg")

# Split image into R, G, B channels

B = img[:,:,0].astype("int16")
G = img[:,:,1].astype("int16")
R = img[:,:,2].astype("int16")


# Calculate ExG (2G - R - B)
exg = 2*G-R-B
exg = numpy.clip(exg,0,255).astype("uint8")

# Filter with threshold values
_, mask = cv2.threshold(exg,60,255, cv2.THRESH_BINARY)
#Display
cv2.imshow("Test image",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
