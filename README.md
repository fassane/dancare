
# Dancare, detection de la Rétinopathie Diabétique
![HeaderImage](github_images/logo.png) 


## Introduction
*Dancare*, une platefome de Détection de la Rétinopathie Diabétique en utilisant le deep learning.



## Technos utilisées
*Python*, *Django*, *Tensorflow*, *Keras*, *PyTorch*, *Sass*, *JQuery*


## Contenu

**Page d'acceuil:** Présentation, 

**Page Fonctionnalités:** Modèles de données

**Page à propos:** Tout sur la plateforme

**Page Demo et Test:** Démo de la solution


## Captures d'écran

### Acceuil | Inteface prinpale
<p align = "left" >
  <img width="350" height="230" src="github_images/home-1.png">
  <img width="350" height="230"  src="github_images/home-2.png"> 
  <img width="350" height="230" src="github_images/home-3.png"> 
  <img width="350" height="230" src="github_images/home-4.png"> 
</p>

### Fonctionnalités | Procédures
<p align = "left" >
  <img width="350" height="230" src="github_images/fonction-1.png">
  <img width="350" height="230"  src="github_images/fonction-2.png"> 
</p>

### A propos | Tout 
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




## Mise en place du projet


### Cloner le projet
```
$ git clone https://github.com/fassane/dancare
```

### Création de l'environnement virtuel

#### Linux
```
$ cd dancare
$ python3 -m venv venv
$ source venv/bin/activate
```
#### Windows
```
$ cd dancare
$ pip install virtualenv
$ virtualenv venv
$ .\venv\Scripts\activate
```

### Installation des libraires
```
$ pip install pip --upgrade
$ pip intall setuptools --upgrade
$ pip install django
$ pip install -r requirements.txt
```


### Important

Présentement, les modèles ont été entrainé depuis les données de la compétiton
ATPOS sur kaggle https://www.kaggle.com/competitions/aptos2019-blindness-detection/data, Tensorflow également. 
Trouver ce modèle résultant dans `diab_retina_app/model`.


### Visualisation de la plateforme
```
$ python manage.py runserver
ou
$ python manage.py runserver 0.0.0.0:8000
ou
$ python manage.py runserver 0.0.0.0:port
```
Aller sur votre navigateur et taper `localhost:8000` ou `localhost:2100`, ou `adresse-ip:port` sur votre réseau local.


### Utilisation

Aller a la page de démo, téléverser une image d'oeil saine ou suceptible de
contenir des sequelles de *réthinopathie diabétique* et procéder au test.
Toutefois, nous vous conseillons d'utiliser les images du dossier 
`diab_retina_app/test`



## Aide et autres

#### Apports
Vous etes libre de télécharger le projet et le modifier comme bon vous semble

#### Aide
Pour tout, `fassanebolly@gmail.com` ou encore via
`ludvlavonou@gmail.com`

