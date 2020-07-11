from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.conf import settings
from django import forms
from account.models import User
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class UpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'bio', 'pic', 'groups')