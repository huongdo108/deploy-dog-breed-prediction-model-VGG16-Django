# Dog breed prediction model deployment with VGG16 and Django

## Overview

In this project, I use transfer learning with VGG16 to build a dog breed prediction model, and build a Django web application where user can upload a dog's image to get prediction. 

I fine-tuned the top layer of pretrained VGG16 to fit in the dataset classification problem. The parameters of lower layers of VGG16 are freezed during training, only the top layer's parameters are trained.

## Data

The data conprises images of 133 breeds of dogs.




## How to run 

### Create virtual environment 
```
python -m venv env
```

### Activate vitual environment
```
source env/Scripts/activate
```

### Install required packages and their dependecies 
```
pip install -r requirements.txt
```

### Run notebook with virtual environment
From inside the environment install ipykernel using pip:
```
pip install ipykernel
```

Install a new kernel
```
ipython kernel install --user --name=env
```

Start jupyter, create a new notebook and select the kernel that lives inside your environment.

### Preprocess data and train the model

Download the data from <a href="https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip">here</a> and put data in **data** folder

Run notebook vgg16.ipynb to preprocess data, train model, and save trained parameters.

Move the trained parameters file **trained_VGG16Net.pt** to **MLapp** folder

### Run Django app locally

Front page

<img src="https://github.com/huongdo108/deploy-dog-breed-prediction-model-VGG16-Django/blob/master/images/frontpage.PNG" align="centre">

Upload image and get to the prediction

<img src="https://github.com/huongdo108/deploy-dog-breed-prediction-model-VGG16-Django/blob/master/images/prediction.PNG" align="centre">





