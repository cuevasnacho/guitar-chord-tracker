import numpy as np


CHORDS = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
CHORDS_DATA = [
    [[514, 352], [475, 316], [407, 311], [357, 303], [398, 403]],
    [[493, 313], [429, 288], [415, 324], [367, 338], [368, 381]],
    [[514, 305], [460, 261], [411, 262], [387, 281], [374, 314]],
    [[471, 294], [432, 220], [392, 273], [343, 273], [328, 296]],
    [[436, 289], [372, 257], [302, 265], [355, 333], [383, 407]],
    [[544, 282], [481, 254], [406, 266], [389, 289], [383, 305]],
    [[391, 301], [345, 227], [285, 286], [271, 306], [269, 333]]
]


def normalize_data(data):
    data_array = np.array(data, dtype=float)
    data_array[:, 1:] /= np.max(data_array[:, 1:])
    centroid = np.mean(data_array[:, 1:], axis=0)
    data_array[:, 1:] -= centroid
    return data_array


def compute_distance_features(data):
    num_landmarks = len(data)
    distance_features = []
    for i in range(num_landmarks):
        for j in range(i + 1, num_landmarks):
            dist = np.linalg.norm(data[i] - data[j])
            distance_features.append(dist)
    return distance_features


if __name__ == '__main__':
    normalized_data = []
    for chord in CHORDS_DATA:
        normalized_data.append(
            normalize_data(chord)
        )

    print(60*'=')
    featured_data = compute_distance_features(normalized_data)
    print(featured_data)
