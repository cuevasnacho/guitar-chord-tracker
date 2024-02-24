import numpy as np
import cv2
import time
import models.hand_detector as htm
from utils.misc import (compute_distance_features, normalize_data, print_screen)
from utils.constants import (SCREEN_WIDTH, SCREEN_HEIGHT,
                             MUSIC_HAND_IDS, CHORDS_DATA, CHORDS)


THRESHOLD = 60

def capture_init():
    cap = cv2.VideoCapture(0)
    cap.set(3, SCREEN_WIDTH)
    cap.set(4, SCREEN_HEIGHT)
    return cap


def show_fps(img, ptime):
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    return ptime


def process_chords(data):
    normalized_data = normalize_data(data)
    return compute_distance_features(normalized_data)


def initialize_chords_data(data):
    featured_data = []
    for chord in data:
        featured_data.append(
            process_chords(chord)
        )
    return featured_data


def nearest_neighbor_matching_live(live_features, patterns_features, patterns_labels):
    min_distance = float('inf')
    best_match = None
    
    for pattern_label, pattern_features in zip(patterns_labels, patterns_features):
        distance = np.linalg.norm(live_features - pattern_features)
        if distance < min_distance:
            min_distance = distance
            best_match = pattern_label
            
    return best_match, min_distance


if __name__ == '__main__':
    cap = capture_init()
    ptime = 0

    detector = htm.HandDetector(detection_con=0.75)
    patterns_data = initialize_chords_data(CHORDS_DATA)

    while cap.isOpened():
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list = detector.find_position(
            img,
            draw=False,
            tip_ids=MUSIC_HAND_IDS,
            show_id=False
        )

        if lm_list:
            captured_data = process_chords(lm_list)
            match, distance = nearest_neighbor_matching_live(
                captured_data,
                patterns_data,
                CHORDS
            )
            if distance < THRESHOLD:
                print_screen(img, match, org=(40, 50), scale=4, color=(0, 255, 0), thickness=3)

        cv2.imshow("Guitar Chord Tracker", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
