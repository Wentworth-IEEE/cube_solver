import tensorflow as tf
from cube import Cube
import scramble_recog


# Defining scrambled state
main_cube = Cube()
for side in main_cube.colors:
    main_cube.set_side(side, scramble_recog.gen_side(side))

# Tensorflow

with tf.Session() as session:
    pass
    