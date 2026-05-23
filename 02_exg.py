# Test file for Exg
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

#Display
cv2.imshow("Test image",exg)
cv2.waitKey(0)
cv2.destroyAllWindows()
