# imports
import numpy as np
import pandas as pd

# read dataset
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/cl_thyroid_conditions.csv')

# suffle data
cl_data = np.array(data)
m, n = cl_data.shape
np.random.shuffle(cl_data)                          # shuffle data
train_data = cl_data.T

# assign input and output
X_train = train_data[0:n-1].T                       # get input train data
Y_train = np.expand_dims(train_data[-1], axis=-1)   # get output train data

# activation function
# sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# derivative of sigmoid
def sigmoid_deriv(x):
    return x * (1 - x)

# mean squared error formula
def mean_squared_error(y_true, y_pred):
    return np.square(np.subtract(y_true,y_pred)).mean()

# initiate parameters
def __init__(X_train, Y_train, alpha):
    X   = np.array(X_train)                     # input
    Y   = np.array(Y_train)                     # output
    A   = alpha                                 # learning rate    
    W1  = np.random.rand(n-1, 10) - 0.5         # nodes in hidden layer   (516 x 7) * (7 x 10) = (516 x 10)
    W2  = np.random.rand(10, 1) - 0.5           # nodes in output layer   (516 x 10) * (10 x 1) = (516 x 1)
    return X, Y, A, W1, W2

# feedforward propagate
def feedforward(X, Y, W1, W2):
    # step 4
    Z1_in = X.dot(W1)
    Z1 = sigmoid(Z1_in)
    # step 5
    Z2_in = Z1.dot(W2)
    Z2 = sigmoid(Z2_in)
    return Z1_in, Z1, Z2_in, Z2

# backword propagate
def backprop(Z1_in, Z1, Z2_in, Z2, W1, W2, X, Y):
    # step 6
    dZ2_in = Y - Z2
    dZ2 = dZ2_in * sigmoid_deriv(Z2)
    # step 7
    dZ1_in = dZ2.dot(W2.T)
    dZ1 = dZ1_in * sigmoid_deriv(Z1)
    # get changes in weight
    dW2 = Z1.T.dot(dZ2) / m
    dW1 = X.T.dot(dZ1) / m
    return dZ2, dZ1, dW2, dW1

# update parameters
def update_param(W1, W2, dW2, dW1, A):
    # weights update
    W2 += dW2 * A
    W1 += dW1 * A
    return W1, W2

# nueral network
def __MAIN__(X_train, Y_train, alpha, epoch):
    X, Y, A, W1, W2 = __init__(X_train, Y_train, alpha)
    for i in range(epoch):
        Z1_in, Z1, Z2_in, Z2 = feedforward(X, Y, W1, W2)                       # forward propagate
        dZ2, dZ1, dW2, dW1 = backprop(Z1_in, Z1, Z2_in, Z2, W1, W2, X, Y)      # backword propagate
        W1, W2 = update_param(W1, W2, dW2, dW1, A)                             # weights update 
        loss = mean_squared_error(Y_train, Z2)
        if (i % 10 == 0):
            print("Iteration: ", i)
            print("Loss: ", loss)
            print("Percentage:", (1-loss)*100)
            print("\n")

# train data
__MAIN__(X_train, Y_train, 0.5, 5000)
