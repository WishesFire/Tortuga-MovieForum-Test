from django import forms
from .models import RatingStar, MARKS_RATING


class RateForm(forms.ModelForm):
    rate = forms.ChoiceField(choices=MARKS_RATING, widget=forms.Select(), required=True)

    class Meta:
        model = RatingStar
        fields = ('rate', )
