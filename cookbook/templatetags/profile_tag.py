from django import template
from cookbook.models import Recipe, AuthorUser

register = template.Library()


@register.simple_tag
def recipe_author(recipe_all, author_user, username):
    user_recipe = author_user.filter(user_username__contains=username)
    recipe = []
    for i in user_recipe:
        recipe.append(recipe_all.get(recipe_name__contains=i.recipe_name))
    return recipe
