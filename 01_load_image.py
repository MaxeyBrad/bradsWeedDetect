# Script to load image
# Brad Maxey 2026

import cv2

# Load image from disk
img = cv2.imread("images/leaf.jpeg")

# Sanity check - imread returns None id the path is wrong
if img is None:
	raise FileNotFoundError("Could not load image - check the path")

# Inpect the image
print(f"Shape: {img.shape}")
print(f"Dtype: {img.dtype}")

# Display it 
cv2.imshow("Test image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
