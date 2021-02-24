# Convolutional-Neural-Network

An introduction into CNN. A small project to classify fruits into 4 different categories. Pillow library is used to open,manipulate and save images and xml parser is used to obtain information on the images. Images are resized to 32x32. Labels are one-hot encoded before being sent to the network. 

Two convolutional blocks are used with 2 convolutional 2D layers(with padding and ReLU activation function) followed by max pooling layer(2x2 with stride 2) in each block. The second block has a dropout layer with value 0.25. Lastly, there is the full-connected classifier where the image matrix is flattened before going throuth a dense layer with ReLU activation function. Another dropout layer with value 0.5 is added before going through the final dense layer with Softmax activation function. Categorical crossentropy is used as loss function and 'adam' is chosen as the optimization technique.

The dataset will go through 35 epochs and 20% of train set is set aside as validation set. Graphs plotted will show the accuracy/loss per epoch.
