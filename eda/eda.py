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