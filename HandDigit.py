import tensorflow as tf
from os import path, getcwd, chdir

# DO NOT CHANGE THE LINE BELOW. If you are developing in a local
# environment, then grab mnist.npz from the Coursera Jupyter Notebook
# and place it inside a local folder and edit the path to that location
path = f"{getcwd()}/../tmp2/mnist.npz"

#function to train model
def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if(logs.get('acc')>0.99):
                print("\nReached 99% accuracy so cancelling training!")
                self.model.stop_training = True

    callbacks = myCallback()

    mnist = tf.keras.datasets.mnist

    (x_train, y_train),(x_test, y_test) = mnist.load_data(path=path)
    
    x_train=x_train/255.0
    x_test=x_test/255.0
    
    model = tf.keras.models.Sequential([
         tf.keras.layers.Flatten(),
         tf.keras.layers.Dense(512, activation=tf.nn.relu),
         tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # model fitting
    history = model.fit(x_train, y_train, epochs=9, callbacks=[callbacks]
    )
    # model fitting
    print( history.epoch, history.history['acc'][-1])
    model.evaluate(x_test,y_test)
    classifications = model.predict(x_test)
    print(classifications[0])
    print(y_test[0])
