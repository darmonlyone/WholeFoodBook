# Organic Recipe [![Build Status](https://travis-ci.com/darmonlyone/WholeFoodBook.svg?branch=master)](https://travis-ci.com/darmonlyone/WholeFoodBook)[![codecov](https://codecov.io/gh/darmonlyone/WholeFoodBook/branch/master/graph/badge.svg)](https://codecov.io/gh/darmonlyone/WholeFoodBook)

Organic Recipe is a recipe book website which you can create your own digital recipe books using recipes from many well-known brands and chefs, combining with your own ideas. Not only create your own recipe, but also provide a lot of recipes from other members of our website and you can communicate with other members by giving rate or leaving any comments on their recipe too.

Check [Whole-Food-Cookbook](http://whole-food-cookbook.herokuapp.com/) out and ready for cooking with our good recipes.

## Project plan
We assign our teammate works by using [Asana Application](https://app.asana.com/). You can see our [project iteration](https://app.asana.com/0/867060982847769/867060982847769)
and [develop plan](https://app.asana.com/0/0/869948396459242).

## Design
Adobe XD is used for designing part. You can look out our [application design here](https://xd.adobe.com/spec/e6dedd13-b89d-4e4f-7e9e-1559692182b9-90ef/).

## Development
Website is developed by Django web framework for create website in html and python3 platform. We use Heroku for deploying our application and Travis Ci for building testing. 
We also user codecov to checkout code coverage of this application.

- [Travis Ci](https://travis-ci.com/darmonlyone/WholeFoodBook)
- [Issue tracker](https://github.com/darmonlyone/WholeFoodBook/issues)
- [codecov](https://codecov.io/gh/darmonlyone/WholeFoodBook/)

## Installation
This document gives the instructions to install this application to your computer.

1. Install python to your OS.
    - [Python 3.6](https://www.python.org/downloads/) 
    
2. Clone this repositories
    
    ```
    $ git clone https://github.com/darmonlyone/WholeFoodBook.git
    ```
3. Chang directory to `WholeFoodBook/` and install virtualenv.

    Install virtualenv
    ```angular2html
    $ pip3 install virtualenv 
    $ virtualenv venv 
    ```
4. Activate virtualenv
    - Mac OS or Ubuntu
     ```
     $ source env/bin/activate
     ```
    - Window OS
    ```
     $ env/bin/activate
     ```
    Install all requirements to your `venv` with this command. 
    ```
    (venv) $ pip install -r requirements.txt
    ```
    This command use for install all requirement library to your python source for running this program.

## Running
    
Running the program using python command. If you wasn't activate `venv` please look on installation before running.
```
(venv) $ python manage.py runserver
```
    
If program cause `SyntaxError`. You can try this command to detect your program to run with **Python 3**.
```
(venv) $ python3 manage.py runserver
``` 
    
## Member
- **Manusporn Fukkham** 6010546702 [@darmonlyone](https://github.com/darmonlyone)
- **Pichaaun Popukdee** 6010545862 [@pichqning](https://github.com/pichqning)
- **Raksani Kunamas** 6010546711 [@raksani](https://github.com/Raksani)
- **Thaksina jansaengsri** 6010545765 [@thaksina](https://github.com/Thaksina)
