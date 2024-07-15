# Example 10.13 Text generation from model trained in Example 10.12
# Modified based on:
# https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/
# Text Generation With LSTM Recurrent Neural Networks in Python with Keras
# Larger LSTM Network to Generate Text for Alice in Wonderland
import numpy
import sys
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils



# load ascii text and covert to lowercase
# prepare the dataset of input to output pairs encoded as integers
def get_textdata(filename):
        raw_text = open(filename, 'r', encoding='utf-8').read()
        raw_text = raw_text.lower()
        # create mapping of unique chars to integers
        chars = sorted(list(set(raw_text)))
        char_to_int = dict((c, i) for i, c in enumerate(chars))
        int_to_char = dict((i, c) for i, c in enumerate(chars))
        # summarize the loaded data
        n_chars = len(raw_text)
        n_vocab = len(chars)
        print ("Total Characters: ", n_chars)
        print ("Total Vocab: ", n_vocab)

        seq_length = 100
        dataX = []
        dataY = []
        for i in range(0, n_chars - seq_length, 1):
                seq_in = raw_text[i:i + seq_length]
                seq_out = raw_text[i + seq_length]
                dataX.append([char_to_int[char] for char in seq_in])
                dataY.append(char_to_int[seq_out])
        n_patterns = len(dataX)
        print ("Total Patterns: ", n_patterns)
        # reshape X to be [samples, time steps, features]
        X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
        # normalize
        X = X / float(n_vocab)
        # one hot encode the output variable
        y = np_utils.to_categorical(dataY)
        return X, y, dataX,int_to_char,n_vocab

# define the LSTM model
def get_model(X, y):
        model = Sequential()
        model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(256))
        model.add(Dropout(0.2))
        model.add(Dense(y.shape[1], activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        # define the checkpoint
        filepath="weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
        checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        callbacks_list = [checkpoint]
        return model,callbacks_list
def get_prediction(filename,dataX,int_to_char,n_vocab):
        model.load_weights(filename)
        model.compile(loss='categorical_crossentropy', optimizer='adam')
        # pick a random seed
        start = numpy.random.randint(0, len(dataX)-1)
        pattern = dataX[start]
        print ("Seed:")
        print ("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
        # generate characters
        for i in range(1000):
          x = numpy.reshape(pattern, (1, len(pattern), 1))
          x = x / float(n_vocab)
          prediction = model.predict(x, verbose=0)
          index = numpy.argmax(prediction)
          result = int_to_char[index]
          seq_in = [int_to_char[value] for value in pattern]
          sys.stdout.write(result)
          pattern.append(index)
          pattern = pattern[1:len(pattern)]
        print ("\nDone.")
# Main function
filename = "wonderland.txt"
X,y,dataX,int_to_char,n_vocab = get_textdata(filename)
model,callbacks_list = get_model(X, y)

# load the network weights and get prediction
filename = "weights-improvement-49-1.3079-bigger.hdf5"
get_prediction(filename,dataX,int_to_char,n_vocab)
