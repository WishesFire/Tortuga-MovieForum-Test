from django import forms


class SearchForm(forms.ModelForm):
    query = forms.CharField()