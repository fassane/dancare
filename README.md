
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

### Page Acceuil
<p align = "left" >
  <img width="350" height="230" src="github_images/home-1.png">
  <img width="350" height="230"  src="github_images/home-2.png"> 
  <img width="350" height="230" src="github_images/home-3.png"> 
  <img width="350" height="230" src="github_images/home-4.png"> 
</p>

### Page Fonctionnalités
<p align = "left" >
  <img width="350" height="230" src="github_images/fonction-1.png">
  <img width="350" height="230"  src="github_images/fonction-2.png"> 
</p>

### Page A propos
<p align = "left" >
  <img width="350" height="230" src="github_images/about-1.png"> 
</p>

### Page Démonstration 
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
$ sudo apt install python3-venv
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
ATPOS sur kaggle https://www.kaggle.com/competitions/aptos2019-blindness-detection/data, Tensorflow également. <br/>
Trouver le modèle résultant dans `diab_retina_app/model`.


### Visualisation de la plateforme
```
$ python manage.py runserver
$ python manage.py runserver 0.0.0.0:8000
$ python manage.py runserver 0.0.0.0:port
```
Aller sur votre navigateur et taper `localhost:8000`, ou `adresse-ip:port` sur votre réseau local.


### Utilisation

- Aller à la page de démo 
- Téléverser une image d'oeil saine ou douteuse 
- Procéder au test <br/>
Cependant, nous vous conseillons d'utiliser les images du dossier 
`diab_retina_app/test`



## Conclusion

#### Open source
Vous etes libre de télécharger le projet et de modifier la logique comme bon vous semble.

#### Aide
Pour tout, `fassanebolly@gmail.com` ou encore via
`ludvlavonou@gmail.com`

