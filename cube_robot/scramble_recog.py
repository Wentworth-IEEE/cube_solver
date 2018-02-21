import cv2

filename = 'cube-face.png'

img = cv2.imread(filename)
images_index = []


def avg_color(coords, index):
    x_size = abs(coords[2] - coords[0])
    y_size = abs(coords[3] - coords[1])
    full_size = x_size * y_size
    b_sum = g_sum = r_sum = 0

    image = images_index[index]

    for i in range(x_size):
        for j in range(y_size):
            b_sum += image.item(i, j, 0)
            g_sum += image.item(i, j, 1)
            r_sum += image.item(i, j, 2)

    b_final = b_sum / full_size
    g_final = g_sum / full_size
    r_final = r_sum / full_size

    bgr_final = [b_final, g_final, r_final]

    return bgr_final


def find_color(bgr_input):

    colors = [[255, 255, 255],
              [0, 255, 255],
              [255, 0, 0],
              [0, 255, 0],
              [0, 0, 255],
              [0, 140, 255]]
    similarity = 30
    color_final = None

    for i in range(6):
        b_difference = abs(colors[i][0] - bgr_input[0])  # find color value delta
        g_difference = abs(colors[i][1] - bgr_input[1])
        r_difference = abs(colors[i][2] - bgr_input[2])
        b_bool = b_difference < similarity  # determine is color is sufficiently similar to reference
        g_bool = g_difference < similarity
        r_bool = r_difference < similarity

        if b_bool and g_bool and r_bool:
            color_final = colors_index[i]
            break

    if color_final is None:
        print('Similarity Error')

    return color_final


colors_index = ['W', 'Y', 'B', 'G', 'R', 'O']
scrambled = [[[]]]
positions = [[[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [None, 0], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
             [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [None, 0], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
             [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [None, 0], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
             [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [None, 0], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
             [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [None, 0], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
             [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [None, 0], [[0, 0, 0, 0], 0]],
              [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]]]
# cube:[face:[row:[tile:[coordinates:[x_final, y_final, x_initial, y_initial], image]]]]]

for i in range(6):
    for j in range(3):
        for k in range(3):
            if positions[i][j][k][0] is not None:
                scrambled[i][j][k] = find_color(avg_color(positions[i][j][k][0], positions[i][j][k][1]))
            else:
                scrambled[i][j][k] = colors_index[i]



