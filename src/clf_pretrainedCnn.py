import os
import pandas as pd
# tf tools
import tensorflow as tf
# image processsing
from tensorflow.keras.preprocessing.image import (ImageDataGenerator)
# VGG16 model
from tensorflow.keras.applications.vgg16 import (VGG16)
# layers
from tensorflow.keras.layers import (Flatten, 
                                     Dense,
                                     BatchNormalization) 
from tensorflow.keras import layers
# generic model object
from tensorflow.keras.models import Model
# optimizers
from tensorflow.keras.optimizers.schedules import ExponentialDecay
from tensorflow.keras.optimizers import SGD
#scikit-learn
from sklearn.metrics import classification_report
# for plotting
import numpy as np
import matplotlib.pyplot as plt
# utils plotting function
import sys
sys.path.append(".")
import utils.plotting as pl

def get_data():
    # Load the json metadata (containing the labels)
    test_df = pd.read_json(os.path.join("images", "metadata", "test_data.json" ), lines=True)
    train_df = pd.read_json(os.path.join("images", "metadata", "train_data.json" ), lines=True)
    val_df = pd.read_json(os.path.join("images", "metadata", "val_data.json" ), lines=True)

    # Generator train data
    train_datagen = ImageDataGenerator(horizontal_flip=True,
                                        rotation_range=20,
                                        rescale=1/255
    )
    # Generator test data
    test_datagen = ImageDataGenerator(
                                    rescale=1./255.
    )
    
    images_dir = os.path.join (".")
    # define target size
    TARGET_size = (224, 224)
    # define batch size
    BATCH_size = 32

    # Generating training data
    train_images = train_datagen.flow_from_dataframe(
        dataframe=train_df,
        directory = images_dir,
        x_col ='image_path',
        y_col ='class_label',
        target_size = TARGET_size,
        color_mode ='rgb',
        class_mode ='categorical',
        batch_size = BATCH_size,
        shuffle = True,
        seed = 42,
        subset ='training'
    )

    # Generating test data
    test_images = test_datagen.flow_from_dataframe(
        dataframe = test_df,
        directory = images_dir,
        x_col ='image_path',
        y_col ='class_label',
        target_size = TARGET_size,
        color_mode ='rgb',
        class_mode ='categorical',
        batch_size = BATCH_size,
        shuffle = False
    )

    # Generatig validation data
    val_images = train_datagen.flow_from_dataframe(
        dataframe = val_df, 
        directory = images_dir,
        x_col ='image_path',
        y_col ='class_label',
        target_size = TARGET_size,
        color_mode ='rgb',
        class_mode ='categorical',
        batch_size = BATCH_size,
        shuffle = True,
        seed = 42,
    )

    return train_images, test_images, val_images, test_df

def cnn_classifier(train_images, test_images, val_images):
    # load the VGG16 model without classifier layers
    model = VGG16(include_top=False,
                pooling='avg', 
                input_shape=(224, 224, 3)) # set to fit the size of the indo images
    # mark loaded layers as not trainable (freeze all weights)
    for layer in model.layers: 
        layer.trainable = False
    # add new classifier layers
    flat1 = Flatten()(model.layers[-1].output) # flatten the images
    bn = BatchNormalization()(flat1) # batch normalization layer
    class1 = Dense(256, 
                activation ='relu')(bn)
    class2 = Dense(128, 
                activation = 'relu')(class1)
    output = Dense(15, 
                activation ='softmax')(class2)
    # define new model
    model = Model(inputs = model.inputs, 
                outputs = output)
    # compile model
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate=0.01,
        decay_steps=10000,
        decay_rate=0.9)
    sgd = SGD(learning_rate=lr_schedule)
    model.compile(optimizer=sgd,
                loss='categorical_crossentropy',
                metrics=['accuracy'])
    # summarize model
    print(model.summary())
    # fit model to indo fashion and train model
    history = model.fit(
        train_images, 
        steps_per_epoch = len(train_images),
        validation_data  = val_images,
        validation_steps = len(val_images),
        epochs = 10)
    # Get predictions
    pred = model.predict(test_images)
    pred = np.argmax(pred,axis=1)
    # Map the label
    labels = (train_images.class_indices)
    labels = dict((v,k) for k,v in labels.items())
    pred = [labels[k] for k in pred]

    return history, pred

def report_and_plot(test_df, history, pred):
    # Training and validation history plots
    pl.plot_history(history, 10)
    output_path = os.path.join("out", "train_and_val_plots.png")
    plt.savefig(output_path, dpi = 100)
    print("Plot is saved!")
    # Create classification report
    y_test = list(test_df.class_label)
    report = classification_report(y_test, pred)
    # Save report in "out"
    file_path = os.path.join("out", "classification_report.txt")
    with open(file_path, "w") as f: #"writing" classifier report and saving it
        f.write(report)
    print("Classification report is saved!")

def main():
    # Load and prepare data
    train_images, test_images, val_images, test_df = get_data()
    # train pretrained CNN
    history, pred = cnn_classifier(train_images, test_images, val_images)
    # save classification report and test and validation plot
    report_and_plot(test_df, history, pred)

if __name__ == "__main__":
    main()
