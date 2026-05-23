## Detector with gui


import cv2
from detector import exhsv_mask, find_weeds, draw_results

#img = cv2.imread("images/leaf.jpeg")
cap = cv2.VideoCapture(0)

cv2.namedWindow("Detector", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Detector", 1200, 800)
# Trackbars
cv2.createTrackbar("ExG thresh", "Detector", 60, 255, lambda x: None)
cv2.createTrackbar("Hue min",    "Detector", 35, 180, lambda x: None)
cv2.createTrackbar("Hue max",    "Detector", 85, 180, lambda x: None)
cv2.createTrackbar("Sat min",    "Detector", 40, 255, lambda x: None)
cv2.createTrackbar("Sat max",    "Detector", 255, 255, lambda x: None)
cv2.createTrackbar("Val min",    "Detector", 40, 255, lambda x: None)
cv2.createTrackbar("Val max",    "Detector", 255, 255, lambda x: None)
cv2.createTrackbar("Min area",   "Detector", 100, 2000, lambda x: None)

# Main loop
while True:
    ret, img = cap.read()
    if not ret:
        break
    # Read current slider values
    exg_t = cv2.getTrackbarPos("ExG thresh", "Detector")
    h_min = cv2.getTrackbarPos("Hue min", "Detector")
    h_max = cv2.getTrackbarPos("Hue max", "Detector")
    s_min = cv2.getTrackbarPos("Sat min", "Detector")
    s_max = cv2.getTrackbarPos("Sat max", "Detector")
    v_min = cv2.getTrackbarPos("Val min", "Detector")
    v_max = cv2.getTrackbarPos("Val max", "Detector")
    min_area = cv2.getTrackbarPos("Min area", "Detector")

    # Run detection with current values
    mask = exhsv_mask(
        img,
        exg_thresh=exg_t,
        hsv_lower=(h_min, s_min, v_min),
        hsv_upper=(h_max, s_max, v_max),
    )
    weeds = find_weeds(mask, min_area=min_area)
    output = draw_results(img, weeds)

    # Display
    cv2.imshow("Detector", output)

    # Quit on 'q'
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
