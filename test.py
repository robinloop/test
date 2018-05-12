from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

batch_size = 1024
nb_classes = 3062
nb_epoch = 30

img_rows, img_cols = 48, 48
# number of convolutional filters to use
nb_filters = 64
# size of pooling area for max pooling
nb_pool = 2
# convolution kernel size
nb_conv = 4

weight_decay = 0.0001
cd = Conv2D(32, (4, 4), input_shape=(128, 128, 3), )
Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3))
# print(cd)


# Convolution2D(nb_filters, nb_conv,
#               border_mode='valid',
#               data_format='channels_first',
#               input_shape=(1, img_rows, img_cols))
