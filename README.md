[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Aj7Sf-j_)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10866147&assignment_repo_type=AssignmentRepo)
# Using pretrained CNNs for image classification

## Contribution
The code for this assignment has been developed on my own, but with inspiration from classmates during the class lectures. The function in the scripts ```plotting.py``` in the ```utils``` folder is provided by my teacher Ross.

## Description and purpose
For this assignment, I will use the pretrained CNN called ```VGG16``` from ```tensorflow.keras``` to classify Indian clothing pieces. I switch out the classification layers in VGG16 for some new layers to obtain better results when training it on the ```Indo fashion dataset```. The purpose of the assignment is to train a classifier on the Indo fashion dataset using a pretrained CNN, save the training and validation plots, and save the classification report. 

## Methods
This assignment contains one scripts called ```clf_pretrainedCnn.py```, which is placed in the ```src``` folder. The script loads the json files with metadata as data frames, and uses them to generate train, test, and validation data.  VGG16 is loaded without its classification layers, and the remaining layers are marked as non-trainable. New layers for flattening the input images, batch normalization, classification and output are added to the model. Then the new model is compiled, summarized and fittet to the Indo fashion data, which it trains on. The output of the script is a plot of the loss and accuracy scores for the training and validation data, and a classification report made from the predictions of the model, both saved in the ```out``` folder. 

## Data
I use the ```Indo fashion dataset```, which consists of 106,000 images of both male and female Indian clothing pieces. The images are divided into 15 different classes which represent different clothing categories. In the validation and test data, the 15 classes are equally distributed with 500 images in each class. The data is collected from several large Indian websites. 

### Get the data
Before running the script, please download the dataset (3GB) from Kaggle: https://www.kaggle.com/datasets/validmodel/indo-fashion-dataset. The dataset should be placed as its own folder outside the other folders in the repository.  
NB: I used the data set provided by my teacher, and it’s organized slightly different from the dataset loaded directly from Kaggle. Therefore, when you download the dataset from Kaggle, please create an extra folder inside the ```images``` folder and call it “metadata”. Then place the three .json files in the new ```metadata``` folder. Then upload the ```images``` folder to your coding device. The folder structure should now look like this: 


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
Before running the scripts, you need to install Python 3 and Bash. I created and ran the code using the app “Coder Python 1.73.1” on Ucloud.sdu.dk. Clone the GitHub repository on your device to get started. 

### Install packages
Run “bash setup.sh” from the command line to create a virtual environment and install the required packages in requirements.txt:
    
    bash setup.sh

### Run the scripts
Begin by loading the data as described above under “Get the data”. Then run the script by running “bash run.sh” from the command line to activate the virtual environment, run the code in clf_pretrainedCnn.py, and deactivate the environment:

        bash run.sh

## Discussing of the results
I only trained the model on a small sample of the data, because of its size. Therefore, the trained model is less accurate than it would have been, if it were trained on the whole dataset. I sampled 10,000 images as my training data, 3,000 as test data, and 2,000 as validation data, but despite of me downscaling the data, the accuracy score is 75%. The class with the best accuracy is “blouses” with an accuracy of 92%, and the lowest accuracy is “gowns” with 51%. Looking at the plots, the train and validation curves are running relatively close to each other in both the loss and the accuracy plot, which indicates that the model is performing relatively decent. 

## References
Indo fashion dataset, Rashmi Margani, Kaggle: https://www.kaggle.com/datasets/validmodel/indo-fashion-dataset.