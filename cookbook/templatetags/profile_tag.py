from django import template
from cookbook.models import Recipe, AuthorUser

register = template.Library()


@register.simple_tag
def recipe_author(recipe_model, author_user, username):
    user_recipe = author_user.filter(user_username__exact=username)
    recipe = []
    for i in user_recipe:
        recipe.append(recipe_model.get(recipe_name__contains=i.recipe_name))
    return recipe


@register.simple_tag
def get_last_alias_from_user(author_alias_model, username):
    alias_filtered = author_alias_model.filter(user_username__exact=username)
    return alias_filtered.last()


@register.simple_tag
def is_recipe_owner(author_user_model, recipe_name, username):
    is_owner = author_user_model.filter(user_username__exact=username, recipe_name__exact=recipe_name)
    if is_owner:
        return True
    return False
