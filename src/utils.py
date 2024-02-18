import cv2
import math


def euclidean_distance(x1, y1, x2, y2):
    x_diff = x1 - x2
    y_diff = y1 - y2
    return math.sqrt(x_diff**2 + y_diff**2)


def print_screen(img, text, org=(0, 0), font=cv2.FONT_HERSHEY_PLAIN,
                 scale=2, color=(255, 0, 0), thickness=2):
    cv2.putText(img, str(text), org, font, scale, color, thickness)
