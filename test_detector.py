import cv2
from detector import load_image, exhsv_mask, find_weeds, draw_results

img = load_image("images/leaf.jpeg")
mask = exhsv_mask(img)
weeds = find_weeds(mask)
output = draw_results(img, weeds)

print(f"Found {len(weeds)} weeds")
cv2.imshow("Result", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
