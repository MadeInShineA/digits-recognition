import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import  numpy as np
data = tf.keras.datasets.mnist

(training_images, training_labels), (test_images, test_labels) = data.load_data()

train_datagen = ImageDataGenerator(
    rescale = 1/255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
)


validation_datagen = ImageDataGenerator(rescale=1/255)

test_images = test_images.reshape(10000, 28, 28, 1)
validation_generator = validation_datagen.flow(test_images, test_labels, batch_size=32)

training_images = training_images.reshape(60000, 28, 28, 1)
train_generator = train_datagen.flow((training_images,training_labels),batch_size=32)


##test_images = test_images.reshape(10000, 28, 28, 1)
##train_data_gen.fit(test_images)

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28,1)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_generator,validation_data=validation_generator,steps_per_epoch = len(training_images) //32 , epochs=20)

model.evaluate(test_images,test_labels)
