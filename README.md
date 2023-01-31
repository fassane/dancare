# Dancare, diabetic retinopathy detection
![HeaderImage](github_images/logo.png) 


## Introduction
*Dancare*, a small web application to detect diabetic retinopathy using deep learning.


## Framework and librairies
*Python*, *Django*, *Tensorflow*, *Keras*, *PyTorch*, *Sass*, *JQuery*


## Content

**Home page:** Presentation, 

**Function page:** data models

**About page:** about plateform

**Demo and test page:** Solution


## Screenshoots

### Home 
<p align = "left" >
  <img width="350" height="230" src="github_images/home-1.png">
  <img width="350" height="230"  src="github_images/home-2.png"> 
  <img width="350" height="230" src="github_images/home-3.png"> 
  <img width="350" height="230" src="github_images/home-4.png"> 
</p>

### Function
<p align = "left" >
  <img width="350" height="230" src="github_images/fonction-1.png">
  <img width="350" height="230"  src="github_images/fonction-2.png"> 
</p>

### About
<p align = "left" >
  <img width="350" height="230" src="github_images/about-1.png"> 
</p>

### Demonstration 
<p align = "left" >
  <img width="350" height="230" src="github_images/demo-1.png">
  <img width="350" height="230"  src="github_images/demo-2.png"> 
  <img width="350" height="230"  src="github_images/demo-3.png"> 
  <img width="350" height="230"  src="github_images/demo-4.png"> 
  <img width="350" height="230"  src="github_images/demo-5.png"> 
  <img width="350" height="230"  src="github_images/demo-6.png"> 
</p>




## Setup project

### Clone project
```
$ git clone https://github.com/fassane/dancare
```

### Create virtual environment

#### Linux
```
$ sudo apt install python3-venv
```
```
$ cd dancare
$ python3 -m venv venv
$ source venv/bin/activate
```
#### Windows
```
> python -m pip install virtualenv
```
```
> cd dancare
> virtualenv venv
> .\venv\Scripts\activate
```

### librairies Installation
```
$ pip install pip --upgrade
$ pip install setuptools --upgrade
$ pip install django
$ pip install -r requirements.txt
```


### Important

currently, the model has been trained with kaggle APTPOS competition datas https://www.kaggle.com/competitions/aptos2019-blindness-detection/data. Tensorflow too. <br/>
Find this model in `diab_retina_app/model`.


### Run application
```
$ python manage.py runserver
or
$ python manage.py runserver 0.0.0.0:8000
or
$ python manage.py runserver 0.0.0.0:port
```
Go to your browser and type **localhost:8000**, or **adresse-ip:port** on your local network.


### Utilisation

- Go to demo page
- Upload an healthy or not eye image 
- Start the test <br/><br/>
However, we recommand you to use the images of **diab_retina_app/test** folder



## Conclusion

#### Open source
You are free to download the project and modify the logic as you wish 

#### Help
Reach me on `fassanebolly@gmail.com` or on `ludvlavonou@gmail.com`

