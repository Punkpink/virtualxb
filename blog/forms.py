from dataclasses import fields
from decimal import Clamped
from importlib.resources import contents
from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','content')