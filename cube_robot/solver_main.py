import tensorflow as tf
import pandas as pd
import cube
from scramble_recog import getScrambled

# Defining solved state
cubie_solved = [[['WBO', 'WB', 'WBR'], ['WO', 'W', 'WR'], ['WGO', 'WG', 'WGR']],
                [['BO', 'B', 'BR'], ['O', 'C', 'R'], ['GO', 'G', 'GR']],
                [['YBO', 'YB', 'YBR'], ['YO', 'Y', 'YR'], ['YGO', 'YG', 'YGR']]]        

# Defining scrambled state
# FIXME: face_to_cube was in move_operations, with the class rewrite it might need to be a part of the cube class
cubie_scrambled = face_to_cube(getScrambled())

# Tensorflow

with tf.Session() as session:
    pass
    