import cv2

class scramble_recog:
    filename0 = ''
    filename1 = ''
    filename2 = ''
    filename3 = ''

    img0 = cv2.imread(filename0)  # Import images
    img1 = cv2.imread(filename1)
    img2 = cv2.imread(filename2)
    img3 = cv2.imread(filename3)
    image_dict = {0: img0, 1: img1, 2: img2, 3: img3}
    colors_index = ['W', 'Y', 'B', 'G', 'R', 'O']


    def avg_color(self, coords, index):

        x_size = abs(coords[2] - coords[0])  # Find size of defined region
        y_size = abs(coords[3] - coords[1])
        full_size = x_size * y_size

        b_sum = g_sum = r_sum = 0

        image = self.image_dict[index]  # Reference image from index value

        for i in range(x_size):
            for j in range(y_size):
                b_sum += image.item(i, j, 0)  # Find and sum the value for each of the b, g, and r components for each pixel
                g_sum += image.item(i, j, 1)
                r_sum += image.item(i, j, 2)

        b_final = b_sum / full_size  # Find the average values for each color
        g_final = g_sum / full_size
        r_final = r_sum / full_size

        bgr_final = [b_final, g_final, r_final]  # Saves the average color value to a BGR list

        return bgr_final


    def find_color(self, bgr_input):

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
                color_final = self.colors_index[i]
                break

        if color_final is None:
            print('Similarity Error')

        return color_final


    scrambled = [[[]]]
    positions = [[[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [None, None], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
                [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [None, None], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
                [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [None, None], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
                [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [None, None], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
                [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [None, None], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]],
                [[[[0, 0, 0, 0], 0], [[0, 0, 0, 0], ], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [None, None], [[0, 0, 0, 0], 0]],
                [[[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0], [[0, 0, 0, 0], 0]]]]
    # cube:[face:[row:[tile:[coordinates:[x_final, y_final, x_initial, y_initial], image]]]]]

    def genScrambled(self):
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    if self.positions[i][j][k][0] is not None:  # Check that the tile has coordinates
                        self.scrambled[i][j][k] = self.find_color(self.avg_color(self.positions[i][j][k][0], self.positions[i][j][k][1]))
                    else:
                        self.scrambled[i][j][k] = self.colors_index[i]
        return self.scrambled


    def getScrambled(self):
        return self.genScrambled()


