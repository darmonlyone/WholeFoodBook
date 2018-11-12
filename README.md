# Organic Recipe [![Build Status](https://travis-ci.com/darmonlyone/WholeFoodBook.svg?branch=master)](https://travis-ci.com/darmonlyone/WholeFoodBook)

Organic Recipe is a recipe book website which you can create your own digital recipe books using recipes from many well-known brands and chefs, combing with your own ideas. Not only create your own, but also provide a lot of recipes from other members of our website and you can communicate with other members by giving rate or leaving any comments on their recipe too.

Check [Whole-Food-Cookbook](https://whole-food-cookbook.herokuapp.com/) out and ready for cooking with our good recipes.

## Project plan
We assign our teammate works by using [Asana Application](https://app.asana.com/). You can see our [project iteration](https://app.asana.com/0/867060982847769/867060982847769)
and [develop plan](https://app.asana.com/0/0/869948396459242).

## Design
Adobe XD is used for designing part. You can look out our [application design here](https://xd.adobe.com/spec/e6dedd13-b89d-4e4f-7e9e-1559692182b9-90ef/).

## Develop
Website is developed by Django web framework for create website in html and python3 platform. We use Heroku for deploying our application and Travis Ci for building testing.

- [Travis Ci](https://travis-ci.com/darmonlyone/WholeFoodBook)
- [Issue tracker](https://github.com/darmonlyone/WholeFoodBook/issues)

## Installation
This document gives the instructions to install this application using *Django* and *Python*.

1. Downland python and django to your OS.
    - [Python 3 << 3.6](https://www.python.org/downloads/)  
    - [Django 2](https://docs.djangoproject.com/en/2.1/topics/install/#installing-official-release) 
2. Clone this repositories
    
    ```
    $ git clone https://github.com/darmonlyone/WholeFoodBook.git
    ```
3. Open `WholeFoodBook/` and activate virtualenv.
    - Mac OS or Ubuntu
     ```
     $ source env/bin/activate
     ```
    - Window OS
     ```
     $ env/bin/activate
     ```
        
    If your program not working very well and require some installation on step 4, come back on this step and
    try out this command.     
    ```
    $ pip install -r requirement.txt
    ```
    This command use to install all requirement to your python source for running program.

4. Running the program using python 3.
    ```
    $ python manage.py runserver
    ```
    
    If program cause `SyntaxError`. You can try this command for running it. To detect your program to **Python 3**.
    ```
    $ python3 manage.py runserver
    ``` 
    
## Member
- **Manusporn Fukkham** 6010546702 [@darmonlyone](https://github.com/darmonlyone)
- **Pichaaun Popukdee** 6010545862 [@pichqning](https://github.com/pichqning)
- **Raksani Kunamas** 6010546711 [@raksani](https://github.com/Raksani)
- **Thaksina jansaengsri** 6010545765 [@thaksina](https://github.com/Thaksina)
