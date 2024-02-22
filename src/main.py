import cv2
import time
import models.hand_detector as htm
from utils.misc import euclidean_distance, print_screen
from utils.constants import TIP_IDS, SCREEN_WIDTH, SCREEN_HEIGHT, MUSIC_HAND_IDS


def fingers_counter(img, lm_list):
    fingers = []

    if lm_list[TIP_IDS[0]][1] > lm_list[TIP_IDS[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    for id in range(1, 5):
        if lm_list[TIP_IDS[id]][2] < lm_list[TIP_IDS[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    total_fingers = fingers.count(1)
    print(total_fingers)

    cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
    print_screen(img, str(total_fingers),
                 org=(45, 375), thickness=25, scale=10)


def thumb_index_distance(lm_list):
    thumb = lm_list[TIP_IDS[0]]
    index = lm_list[TIP_IDS[1]]
    distance = euclidean_distance(
        thumb[1], thumb[2],
        index[1], index[2]
    )
    return distance


def finger_potentiometer(img, lm_list):
    distance = thumb_index_distance(lm_list)
    if distance < 30:
        percentage = 0.00
    elif distance > 230:
        percentage = 100.00
    else:
        percentage = round((distance - 30)/2, 2)
    bar_width = int((percentage/100)*SCREEN_WIDTH)
    cv2.rectangle(img, (0, 0), (bar_width, 20), (0, 255, 0), cv2.FILLED)
    print_screen(img, text=percentage, org=(45, 375))


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


if __name__ == '__main__':
    cap = capture_init()
    ptime = 0

    detector = htm.HandDetector(detection_con=0.5)

    while cap.isOpened():
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list = detector.find_position(img, draw=False, tip_ids=MUSIC_HAND_IDS)
        ptime = show_fps(img, ptime)

        if lm_list:
            ptime = show_fps(img, ptime)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()
