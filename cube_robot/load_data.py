import tensorflow as tf
import pandas as pd

# Load training data
training_data_df = pd.read_csv('training_data.csv', dtype='object')

# Parse training data
x_training = training_data_df[['scramble']].values
y_training = training_data_df[['solution']].values

# load test data
test_data_df = pd.read_csv('test_data.csv', dtype='object')

# Parse test data
x_training = training_data_df[['scramble']].values
y_training = training_data_df[['solution']].values

