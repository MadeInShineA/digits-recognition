import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import numpy as np
class Mycallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if logs.get("accuracy") > 0.97:
            print("\nReached 95% accuracy so cancelling training!")
            self.model.stop_training = True

callback = Mycallback()

data = tf.keras.datasets.mnist

(training_images, training_labels), (test_images, test_labels) = data.load_data()

train_datagen = ImageDataGenerator(
    rescale = 1/255,
    width_shift_range=0.3,
    height_shift_range=0.3
)


validation_datagen = ImageDataGenerator(
    rescale=1/255,
    width_shift_range=0.3,
    height_shift_range=0.3)

test_images = test_images.reshape(10000, 28, 28, 1)
validation_generator = validation_datagen.flow(test_images, test_labels, batch_size=32)

training_images = training_images.reshape(60000, 28, 28, 1)
train_generator = train_datagen.flow((training_images,training_labels),batch_size=32)


##test_images = test_images.reshape(10000, 28, 28, 1)
##train_data_gen.fit(test_images)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation="relu", input_shape=(28, 28, 1)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(16, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(132, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_generator,validation_data=validation_generator,steps_per_epoch = len(training_images) //32 , epochs=100, callbacks=[callback])

model.evaluate(test_images,test_labels)

model.save("final-cnn-digits-model")


