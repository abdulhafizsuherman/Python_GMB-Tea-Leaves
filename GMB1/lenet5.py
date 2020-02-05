# import packages yang penting
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K


# membuat class lenet

class LeNet:

    @staticmethod  # for namespace and organization purposes
    def build(numChannels, imgRows, imgCols, numClasses,
              activation="relu", wigthsPath=None):
        # inisialisasi model
        model = Sequential()
        inputShape = (imgRows, imgCols, numChannels)
        # mendefinasikan set part pertama dari CONV => ACTIVATION => Pool layers
        model.add(Conv2D(20, 5, padding = "same",
                         input_shape = inputShape))
        model.add(Activation(activation))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

