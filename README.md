
# Dancare Diabetic Retinopathy detect
![HeaderImage](github_images/logo.png) 


## Introduction
Détection de la Rétinopathie Diabétique en utilisant le deep learning

Testé sur Google Chrome version 109.0.5414.74


## Technology and Architecture
Pyhton, Django, Tensorflow, Keras, Werkzug


## Fonctionnalites

**Page d'acceuil:** Splash, Login, Register

**Home Screen:** App operations that can do

**Exchange Screen:** List of crypto exhanges

**Portofolio Screen:** Information of user, Button to show portofolio

**Chatbot Screen:** Chat with Dia bot, 

## Captures d'écran

### Page d'acceuil | Inteface prinpale
<p align = "left" >
  <img width="250" height="500" src="github_images/ ">
  <img width="250" height="500"  src="github_images/ "> 
  <img width="250" height="500" src="github_images/ "> 
</p>

### Home | Exchange | Portofolio
<p align = "left" >
  <img width="250" height="500" src="github_images/ ">
  <img width="250" height="500"  src="github_images/ "> 
  <img width="250" height="500" src="github_images/ "> 
</p>

### Chatbot | Chat
<p align = "left" >
  <img width="250" height="500" src="github_images/prechat.jpeg">
  <img width="250" height="500"  src="github_images/chat.jpeg"> 
</p>

### Choose image | Solde
<p align = "left" >
  <img width="250" height="500" src="github_images/chooseimg.jpg">
  <img width="250" height="500"  src="github_images/solde.jpg"> 
</p>

## Setup

#### Requirements
* Basic knowledge about ES6.
* Basic knowledge about JavaScript.
* Basic knowledge about React Native.
* Basic knowledge about Android and Android Studio.
* Android SDK Tools 23.0.5 or higher.
* Android version >= 5.0 (API level 21).

#### Project
1. Download or clone and open with e.g Visual Studio Code.
2. Make sur you have an emulator or a phone connected.
3. In your terminal:
    * If you have react-native cli installed globally, run `react-native run-android`
    * If you don't have it installed, run `npx react-native run-android`

## Help
If needed reach me on fassanebolly@gmail.com

Instructions to be followed
--------------------------------------------------

Install the below required packages:

django - (pip install django)
tensorflow - (pip install tensorflow)
pillow - (pip install pillow || pip install PIL)
numpy (pip install numpy)

===================================================

Configuration to be made:

Inside diabetic_retinopathy -> settings.py at last you have to put your local path to output directory currently it is my local path 

===================================================

Note: 

Currently the models have been trained using tesnsorflow keras you can find the models inside diab_retina_app -> model folder

===================================================

To execute the project run the below command:

python manage.py runserver

===================================================

Input:

choose the test image from the test directory given inside the project ie; diab_retina_app->test
Training images are not included in the folder since it's a large collection 
The same images you have sent have been used for training

===================================================

You are free to edit the front-end/processing logic as per your need

===================================================
