import cv2

filename0 = 'test_image.jpg'
filename1 = ''
filename2 = ''
filename3 = ''

img0 = cv2.imread(filename0)  # Import images
img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)
img3 = cv2.imread(filename3)
image_dict = {0: img0, 1: img1, 2: img2, 3: img3}
colors_index = ['W', 'Y', 'B', 'G', 'R', 'O']

# {'side": (x_min, y_min, camera)
side_coords = {'W': [[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
                     [(0, 0, 0), None, (0, 0, 0)],
                     [(0, 0, 0), (0, 0, 0), (0, 0, 0)]],
               'Y': [[(0, 0, 0), (0, 0, ), (0, 0, 0)],
                     [(0, 0, 0), None, (0, 0, 0)],
                     [(0, 0, 0), (0, 0, 0), (0, 0, 0)]],
               'B': [[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
                     [(0, 0, 0), None, (0, 0, 0)],
                     [(0, 0, 0), (0, 0, 0), (0, 0, 0)]],
               'G': [[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
                     [(0, 0, 0), None, (0, 0, 0)],
                     [(0, 0, 0), (0, 0, 0), (0, 0, 0)]],
               'R': [[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
                     [(0, 0, 0), None, (0, 0, 0)],
                     [(0, 0, 0), (0, 0, 0), (0, 0, 0)]],
               'O': [[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
                     [(0, 0, 0), None, (0, 0, 0)],
                     [(0, 0, 0), (0, 0, 0), (0, 0, 0)]]
               }

def avg_color(coords, index):
    box_size = 20
    full_size = box_size ** 2

    b_sum = g_sum = r_sum = 0

    image = image_dict[index]  # Reference image from index value

    for i in range(box_size):
        for j in range(box_size):
            # Find and sum the value for each of the b, g, and r components for each pixel
            b_sum += image.item(i, j, 0)
            g_sum += image.item(i, j, 1)
            r_sum += image.item(i, j, 2)

    b_final = b_sum / full_size  # Find the average values for each color
    g_final = g_sum / full_size
    r_final = r_sum / full_size

    bgr_final = [b_final, g_final, r_final]  # Saves the average color value to a BGR list

    return bgr_final

def find_color(bgr_input):
    # Defined values for each of the cube's colors
    colors = [[255, 255, 255],  # White
            [0, 255, 255],    # Yellow
            [255, 0, 0],      # Blue
            [0, 255, 0],      # Green
            [0, 0, 255],      # Red
            [0, 140, 255]]    # Orange
    similarity = 30
    color_final = None  # Default to None

    for i in range(6):
        b_difference = abs(colors[i][0] - bgr_input[0])  # Find color value delta
        g_difference = abs(colors[i][1] - bgr_input[1])
        r_difference = abs(colors[i][2] - bgr_input[2])
        b_bool = b_difference < similarity  # Determine is color is sufficiently similar to reference
        g_bool = g_difference < similarity
        r_bool = r_difference < similarity

        if b_bool and g_bool and r_bool:  # Check if all three color components are similar
            color_final = colors_index[i]
            break

    if color_final is None:
        print('Similarity Error')

    return color_final

def gen_side(side):
    side_data = side_coords[side]
    output = [[None] * 3] * 3
    for i in range(side_data.__sizeof__()):
        for j in range(side_data[i].__sizeof__()):
            if side_data[i][j] is not None:
                output[i][j] = avg_color(side_data[i][j][0:4], side_data[i][j][4])
            else:
                output[i][j] = side
    return output
