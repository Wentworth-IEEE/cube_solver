import tensorflow as tf
import pandas as pd
import move_operations
from scramble_recog import getScrambled

# Defining solved state
cubie_solved = [[['WBO', 'WB', 'WBR'], ['WO', 'W', 'WR'], ['WGO', 'WG', 'WGR']],
                [['BO', 'B', 'BR'], ['O', 'C', 'R'], ['GO', 'G', 'GR']],
                [['YBO', 'YB', 'YBR'], ['YO', 'Y', 'YR'], ['YGO', 'YG', 'YGR']]]

# Defining scrambled state
cubie_scrambled = face_to_cube(getScrambled())

# Tensorflow

# Import training data
training_data_df = pd.read_csv('training_data.csv', dtype='string')

x_training = training_data_df[['scramble']].values
y_training = training_data_df[['solution']].values

with tf.Session() as session:
    pass
