from django import forms


from .models import Category, Book


class SearchInput(forms.widgets.Input):
    input_type = "search"
    template_name = "django/forms/widgets/text.html"


class BookForm(forms.ModelForm):
    category_ids = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=Category.objects.all(),
        initial=[]
    )


class BooksSearchForm(forms.Form):
    name = forms.CharField(required=False, max_length=50, widget=SearchInput)
    categories_set = Category.objects.all()
    categories = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=categories_set,
        required=False)


