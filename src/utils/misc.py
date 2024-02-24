"""
utils.py

This module has various functions for main module

Functions:
- euclidean_distance(x1, y1, x2, y2): Calculate the Euclidean distance between
                                      two points
- print_screen(img, text, org=(0, 0), font=cv2.FONT_HERSHEY_PLAIN,
               scale=2, color=(255, 0, 0), thickness=2): Print text on an image
- normalize_data(data): Normalize data between 0 and 1
- compute_distance_features(data): Calculates distance features
                                                   between points


"""

import cv2
import numpy as np


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
    return np.sqrt(x_diff**2 + y_diff**2)


def normalize_data(data):
    """
    Normalize data between 0 and 1

    Args:
        data ([[int]]): Input data

    Returns:
        [[float]]: Normalized data
    """
    data_array = np.array(data, dtype=float)
    data_array[:, 1:] /= np.max(data_array[:, 1:])
    centroid = np.mean(data_array[:, 1:], axis=0)
    data_array[:, 1:] -= centroid
    return data_array


def compute_distance_features(data):
    """
    Calculates distance features between points

    Args:
        data ([[float]]): Input data

    Returns:
        [float]: Featured distance data
    """
    num_landmarks = len(data)
    distance_features = []
    for i in range(num_landmarks):
        for j in range(i + 1, num_landmarks):
            dist = np.linalg.norm(data[i] - data[j])
            distance_features.append(dist)
    return np.array(distance_features)


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
