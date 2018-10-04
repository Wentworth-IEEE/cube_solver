import tensorflow as tf
import pandas as pd
import move_operations
from scramble_recog import getScrambled

# Defining solved state
cubie_solved = [[['WBO', 'WB', 'WBR'], ['WO', 'W', 'WR'], ['WGO', 'WG', 'WGR']],
                [['BO', 'B', 'BR'], ['O', 'C', 'R'], ['GO', 'G', 'GR']],
                [['YBO', 'YB', 'YBR'], ['YO', 'Y', 'YR'], ['YGO', 'YG', 'YGR']]]

cross_solved = [[['xxx', 'Wx', 'xxx'], ['Wx', 'W', 'Wx'], ['xxx', 'Wx', 'xxx']],
                [['xx', 'x', 'xx'], ['x', 'x', 'x'], ['xx', 'x', 'xx']],
                [['xxx', 'xx', 'xxx'], ['xx', 'x', 'xx'], ['xxx', 'xx', 'xxx']]]          

# Defining scrambled state
cubie_scrambled = face_to_cube(getScrambled())

# Tensorflow

with tf.Session() as session:
    pass
    