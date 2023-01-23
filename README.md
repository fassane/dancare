
# Dancare Diabetic Retinopathy detect
![HeaderImage](github_images/logo.png) 


## Introduction
Détection de la Rétinopathie Diabétique en utilisant le deep learning



## Technologies and Architecture
Pyhton, Django, Tensorflow, Keras, PyTorch


## Contenu

**Page d'acceuil:** Presentation, 

**Page Fonctionnalités:** Modèles de données

**Page à propos:** Tout sur la plateforme

**Page Demo et Test:** Démo de la solution


## Captures d'écran

### Acceuil | Inteface prinpale
<p align = "left" >
  <img width="250" height="500" src="github_images/ ">
  <img width="250" height="500"  src="github_images/ "> 
  <img width="250" height="500" src="github_images/ "> 
</p>

### Fonctionnalités | Procédures
<p align = "left" >
  <img width="250" height="500" src="github_images/ ">
  <img width="250" height="500"  src="github_images/ "> 
  <img width="250" height="500" src="github_images/ "> 
</p>

### A propos | Tout 
<p align = "left" >
  <img width="250" height="500" src="github_images/prechat.jpeg">
  <img width="250" height="500"  src="github_images/chat.jpeg"> 
</p>



## Préréquis

* Connaissance basique de Python.
* Connaissance basique de Django.
* Connaissance basique de Sass.
* Connaissance basique des modeles CNN .
* Connaissance basique de Tensorflow.



## Mise en place

### Suivre les étapes suivantes

#### Cloner le projet
```
$ git clone https://github.com/fassane/dancare
```

#### Mettre en l'environnement virtuel
```
$ cd dancare
$ python3 -m venv venv
$ source venv/bin/activate
```

#### Installation des libraires
```
$ pip install pip --upgrade
$ pip intall setuptools --upgrade
$ pip install django
$ pip install tensorflow
$ pip install pillow || pip install PIL
$ pip install numpy
$ pip install torch
$ pip install torchvision
$ pip install matplolib
$ pip install keras
```

#### Configuration a faire

A la fin du fichier `diabetic_retinopathy/settings.py` vous devez changer le
chemin du fichier.


#### Important

Présentement, les modèles ont été entrainé depuis les données de la compétiton
ATPOS disponible sur *kaggle* via le lien https://www.kaggle.com/competitions/aptos2019-blindness-detection/data. Aussi a l'aide de **Tensorflow**. 
Vous pouvez trouver ces modèles dans le dossier `diab_retina_app/model`.


#### Visualisation de la plateforme
```
$ python manage.py runserver
$ python manage.py runserver 2100 (pour tourner sur le port 2400)
```
Aller dans votre navigateur et taper `localhost:8000` ou `localhost:2100` selon
ce que vous avez entez


#### Utilisation

Aller a la page de démo, téléverser une image d'oeil saine ou suceptible de
contenir des sequelles de *réthinopathie diabétique* et procéder au test.
Toutefois, nous vous conseillons d'utiliser les images du dossier 
`diab_retina_app/test`



## Aide mot de fin

#### Apports et open source

`Vous etes libre de télécharger le projet et le modifier comme bon vous semble`

Pour toute aide, joigner nous sur `fassanebolly@gmail.com` ou encore sur
`ludvlavonou@gmail.com`

