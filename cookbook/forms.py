from django import forms

from cookbook.models import UserAlias


class UserAliasForm(forms.Form):
    user_username = forms.CharField(max_length=100)
    alis_name = forms.CharField(max_length=50)
