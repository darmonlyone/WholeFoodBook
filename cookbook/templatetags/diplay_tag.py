from django import template
from cookbook.models import Recipe

register = template.Library()


@register.simple_tag
def replace_text_space(text):
    return text.replace(" ", "-")


@register.simple_tag
def cut_text_newline(text):
    return text.replace("\n", " ").replace('\r', '')


@register.simple_tag
def get_filter_model_time_tags(model, time_prep):
    return model.filter(time_tags__cook_times=time_prep)


@register.simple_tag
def get_filter_model_equipment_tags(model, equipment):
    return model.filter(equipment_tags__equipment_required=equipment)


@register.simple_tag
def get_filter_model_allergies_tags(model, allergies):
    return model.filter(allergies_tags__allergies_ingredient=allergies)


@register.simple_tag
def get_filter_model_tags(model, time_prep=None, equipment=None, allergies=None):
    return model.filter(time_tags__cook_times=time_prep, equipment_tags__equipment_required=equipment, allergies_tags__allergies_ingredient=allergies)