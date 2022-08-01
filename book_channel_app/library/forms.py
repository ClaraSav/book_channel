from tkinter import Widget
from turtle import textinput
from django import forms

from .models import Category, Book


class BookForm(forms.ModelForm):
    category_ids = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=Category.objects.all(),
        initial=0
    )
