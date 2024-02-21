"""
utils.py

This module has various functions for main module

Functions:
- euclidean_distance(x1, y1, x2, y2): Calculate the Euclidean distance between
                                      two points
- print_screen(img, text, org=(0, 0), font=cv2.FONT_HERSHEY_PLAIN,
               scale=2, color=(255, 0, 0), thickness=2): Print text on an image

"""

import math
import cv2


def euclidean_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points

    Args:
        x1 (int): x coordinate of point 1
        y1 (int): y coordinate of point 1
        x2 (int): x coordinate of point 2
        y2 (int): y coordinate of point 2

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
        text (string): Text to be printed
        org (tuple): Origin coordinates
        font (int): Font type
        scale (int): Font scale
        color (tuple): Font color
        thickness (int): Font thickness
    """
    cv2.putText(img, str(text), org, font, scale, color, thickness)
