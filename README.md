[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Aj7Sf-j_)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10866147&assignment_repo_type=AssignmentRepo)
# Using pretrained CNNs for image classification

## Contributers
I have developed this assignment with contributions from class mates.In the ```utils``` folder is a script called ```plotting.py``` which contains a plotting function. The function is created by my teacher Ross, and we used it in class. I call this script in my of main scripts and use the function to plot the training and validation history plots of the model.

## Description and purpose
In this assignment, I will use the pretrained CNN called VGG16 to from tensorflow keras to be able to train a model that can classify Indian clothing pieces. I switch out the classification layers in VGG16 for some new layers, to obtain better results when trianing it on the Indo fashion dataset. 
The purpose of this assignment is to 
   
1) train a classifier on the Indo fashion data set using a pretrained CNN
2) Save the trainig and validation plots. The plots are saved in the  ```out``` folder. 
3) Save the classification report. The report is saved in the ```out``` folder. 

Further documentation for VGG16 can be found here: https://keras.io/api/applications/vgg/ 

## Methods

This project contains one script called ```clf_pretrainedCnn```, which can be found in the ```src``` folder. The script trains a model to classify pieces of clothing from the  Indo fashion dataset. The script consists of the following parts:

- __get_data()__ loads in the json files with meta data as data frames, and generates train, test and validation data. 
- __train_classifier()__ loads the VGG16 model without the classifier layers and marks the layers in the model as not trainable. Then it adds new classification layers including one layer to flatten the input images, and a layer for batch normalization. Then the model is compiled, summarized and fittet to the Indo fashion dataset. 
- __main()__ 
    - runs the get_data() and train_classifier(). 
    - Then it runs the ```plot_history()``` function from the ```utils```folder and save the plots in the ```out``` folder. 
    - Predict the classes of the images from the trained model, and uses the predictions to make a classification report, which is saved in the ```out``` folder. 

## Data
My model has been trained on the Indo fashion dataset, which consists of 106K images of both male and female Indian clothing pieces. The clothes is divided into 15 different categories. The 15 classes is equally destributed in the validation and test data with 500 images in each class. The data is collected from several large Indian websites.

### Get the data
I haven't included the data in my Github repo because of the size of it (3 GB). Before running the script, please download the Indo fashion data set and save it in the ```in``` folder. 
The data can be accessed and download (3 GB) here: https://www.kaggle.com/datasets/validmodel/indo-fashion-dataset 

__NB__: I used the data set provided by my teacher Ross, and it is organized slightly different from the dataset loaded directly from Kaggle. Therefore, when you download the dataset from  Kaggel, you have to manually create an extra folder inside the ```images``` folder and name it "metadata". Then place the three .json files in the ```metadata``` folder. Now the ```images``` folder contains four folders called ```train```, ```test```, ```val``` and ```metadata```. 
Upload the ```images``` folder to your coding program and place it in the ```in``` folder. Now your folder structure should look like this:

```
- images
    - metadata
        - test_data.json
        - train_data.json
        - val_data.json
    - test
    - train
    - val
```
    
## Usage
### Prerequisites
For the code to run, you must have Bash and Python 3 installed. I created and tested the code using the app "Coder Python 1.73.1" on Ucloud.sdu.dk. 

### Install packages
Run "bash setup.sh" from the commandline to create a virtual environment and install the required packages:
    
    bash setup.sh

### Run the scripts
1) Begin by loading the data as described above under "Get the data". 
2) Run the script by running "bash run.sh" from the commandline to activate the virtual environment, run the code in the clf_pretrainedCnn script, and deactivate the environment:

        bash run.sh

## Discussing of the results
I only trained the model on a random sample of the data set, because of its size. Therefore, the model is less accurate than it could have been, if it was trained on all the data. Still, the results is not that bad. I sampled 10000 images as my training data, 3000 as test data, and 2000 as validation data, but despite me downskaling the data, the accuracy of the model is 75%. The class with the best accuracy is blouses with 92%, andthe lowest accuracy is for gows and it is 51%. Looking at the train and validation plots, the two curves are running relatively close, which indicates that the model is relatively okay. 

## References
Indo fashion dataset, Kaggle: https://www.kaggle.com/datasets/validmodel/indo-fashion-dataset

VGG16, https://keras.io/api/applications/vgg/ 
