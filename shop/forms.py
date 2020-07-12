from django import  forms
from .models import ReviewModel

class  ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ('review',)

        widgets = {
            'review':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'leave review for this product'}),
        }