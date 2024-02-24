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
