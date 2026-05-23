# Detector

import cv2
import numpy

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Couldn't load image: {path}")
    return img

def exg(img):
    B = img[:, :, 0].astype("int16")
    G = img[:, :, 1].astype("int16")
    R = img[:, :, 2].astype("int16")
    result = 2 * G - R - B
    return numpy.clip(result, 0, 255).astype("uint8")


def threshold_mask(grey, value=60):
    _, mask = cv2.threshold(grey, value, 255, cv2.THRESH_BINARY)
    return mask

def hsv_mask(img, lower=(35, 40, 40), upper=(85, 255, 255)):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = numpy.array(lower)
    upper = numpy.array(upper)
    return cv2.inRange(hsv, lower, upper)

def exhsv_mask(img, exg_thresh=60, hsv_lower=(35, 40, 40), hsv_upper=(85, 255, 255)):
    exg_grey = exg(img)
    exg_bin = threshold_mask(exg_grey, exg_thresh)
    hsv_bin = hsv_mask(img, hsv_lower, hsv_upper)
    return cv2.bitwise_and(exg_bin, hsv_bin)

def find_weeds(mask, min_area=100):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    weeds = []
    for c in contours:
        if cv2.contourArea(c) > min_area:
            x, y, w, h = cv2.boundingRect(c)
            cx = x + w // 2
            cy = y + h // 2
            weeds.append((x, y, w, h, cx, cy))
    return weeds

def draw_results(img, weeds):
    output = img.copy()
    for i, (x, y, w, h, cx, cy) in enumerate(weeds):
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(output, (cx, cy), 5, (0, 0, 255), -1)
        cv2.putText(output, f"weed {i+1}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    return output



