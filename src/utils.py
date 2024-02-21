"""
utils.py

This module has various functions for main module

Functions:
- euclidean_distance(x1, y1, x2, y2): Calculate the Euclidean distance between two points
- print_screen(img, text, org=(0, 0), font=cv2.FONT_HERSHEY_PLAIN,
               scale=2, color=(255, 0, 0), thickness=2): Print text on an image

"""

import math
import cv2


def euclidean_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points

    Args:
        x1: x coordinate of point 1
        y1: y coordinate of point 1
        x2: x coordinate of point 2
        y2: y coordinate of point 2

    Returns:
        float: The Euclidean distance between the two points
    """
    x_diff = x1 - x2
    y_diff = y1 - y2
    return math.sqrt(x_diff**2 + y_diff**2)


def print_screen(img, text, org=(0, 0), font=cv2.FONT_HERSHEY_PLAIN,
                 scale=2, color=(255, 0, 0), thickness=2):
    """
    Print text on an image

    Args:
        img (numpy.ndarray): Input image
        text: Text to be printed
        org: Origin coordinates
        font: Font type
        scale: Font scale
        color: Font color
        thickness: Font thickness
    """
    cv2.putText(img, str(text), org, font, scale, color, thickness)
