from django import template
from cookbook.models import Recipe

register = template.Library()


@register.simple_tag
def get_filter_model_time_tags(model, time_prep):
    return model.filter(time_tags=time_prep)


@register.simple_tag
def get_filter_model_equipment_tags(model, equipment):
    return model.filter(equipment_tags=equipment)


@register.simple_tag
def get_filter_model_allergies_tags(model, allergies):
    return model.filter(allergies_tags=allergies)


@register.simple_tag
def get_filter_model_tags(model, time_prep=None, equipment=None, allergies=None):
    return model.filter(time_tags=time_prep, equipment_tags=equipment, allergies_tags=allergies)
