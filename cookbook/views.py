from django.shortcuts import render
from cookbook.models import Recipe


def welcome(request):
    return render(request, 'welcome.html')


def menu(request):
    return render(request, 'menu.html')


def fake_put_db(request):
    r = Recipe(user="Darm", recipe_name="food name",
               recipe_info="love",
               recipe_time=10,
               recipe_type="cookie",
               recipe_fat=12,
               recipe_ingredient="dasdasr",
               recipe_method="asdasd")
    r.save()

# heroku pg:psql
# \d
# SELECT * FROM cookbook_recipe;
