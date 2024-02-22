import sys
sys.path.append('/home/icuevas/Desktop/nacho/guitar-chord-tracker/')

import cv2
import numpy as np
from src.models import csv_handler as csvh


if __name__ == '__main__':
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    csv_handler = csvh.CSVHandler('../data/hand_patterns.csv')
    data = csv_handler.get_data()

    hand_data = []
    for i in range(len(data)//5):
        hand = []
        for j in range(5):
            hand.append(data[i*5+j])
        hand_data.append(hand)

    ctr = 0

    INDEXES = [10, 27, 45, 66, 87, 131, 151]
    NOTES = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']

    note = 0
    for i in INDEXES:
        print(NOTES[note])
        print(hand_data[i])
        note += 1

    for i in hand_data:
        cv2.rectangle(img, (0, 0), (640, 480), (255, 255, 255), thickness=cv2.FILLED)
        cv2.putText(img, f'ctr: {ctr}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        for dot in i:
            cv2.circle(img, (int(dot[1]), int(dot[2])), 15, (255, 0, 255), cv2.FILLED)
        cv2.imshow('ctr', img)

        key = cv2.waitKey(1000)
        ctr += 1
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
