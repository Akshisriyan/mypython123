import tensorflow as tf
from tensorflow import keras
import backend as K
from keras.models import Sequential
from keras.layers import conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, Activation, Input, zeroPadding2D
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator , load_img, img_to_array , array_to_img
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

from keras_preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from keras.datasets import mnist

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report


device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

from google.colab import drive
drive.mount('/content/drive')

# load the data

(trainX, trainY), (testX, testY) = mnist.load_data()

if K.image_data_format() == "channels_first":
    trainX = trainX.reshape(trainX.shape[0], 1, 28, 28)
    testX = testX.reshape(testX.shape[0], 1, 28, 28)
else:
    trainX = trainX.reshape(trainX.shape[0], 28, 28, 1)
    testX = testX.reshape(testX.shape[0], 28, 28, 1)

#scale the data
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0

# convert the labels from integers to vectors
lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)
num_classes = testY.shape[1]

print(num_classes)
print(trainX.shape)
print(trainX.shape[0])

