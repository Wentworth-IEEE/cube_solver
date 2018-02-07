import cv2

filename = 'cube-face.png'

img = cv2.imread(filename)
print(img[100, 100])


def avg_color(image, x_origin, y_origin, x_final, y_final):
    x_size = abs(x_final - x_origin)
    y_size = abs(y_final - y_origin)
    full_size = x_size * y_size
    b_sum = g_sum = r_sum = 0

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
    colors_index = ['W', 'Y', 'B', 'G', 'R', 'O']
    similarity = 30
    color_final = None

    for i in range(6):
        b_difference = abs(colors[i][0] - bgr_input[0])
        g_difference = abs(colors[i][1] - bgr_input[1])
        r_difference = abs(colors[i][2] - bgr_input[2])
        b_bool = b_difference < similarity
        g_bool = g_difference < similarity
        r_bool = r_difference < similarity

        if (b_bool and g_bool and r_bool):
            color_final = colors_index[i]
            break

    if (color_final is None):
        print('Similarity Error')

    return color_final
