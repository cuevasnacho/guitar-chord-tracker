"""
hand_detector.py

Functions for hand detection

Class:
- HandDetector(): Hand Detector handler
"""

import cv2
import mediapipe as mp


class HandDetector():
    """
    Hand Detector handler
    """
    def __init__(self, mode=False, max_hands=2,
                 detection_con=0.5, track_con=0.5):
        """
        Hand Detector initializer

        Args:
            mode (bool):
            max_hands (int): number of hand to be detected
            detection_con (float): detection confidence level
            track_con (float): track confidence level
        """
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, 1,
                                         self.detection_con, self.track_con)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        """
        Find hands in image capture

        Args:
            img (numpy.ndarray): Input image
            draw (bool): Draw hands tracker

        Returns:
            img (numpy.ndarray): Output image
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_lms,
                                               self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_no=0, draw=True,
                      tip_ids=[], show_id=True):
        """
        Find hand spots coordinates

        Args:
            img (numpy.ndarray): Input image
            hand_no (int):
            draw (bool): Draw hand articulations
            tip_ids ([int]): Ids to be tracked
            show_id (bool): Append tip id

        Returns:
            lm_list ([[int]]): Finger coordinates
        """
        lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id in tip_ids:
                    if show_id:
                        lm_list.append([id, cx, cy])
                    else:
                        lm_list.append([cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lm_list
