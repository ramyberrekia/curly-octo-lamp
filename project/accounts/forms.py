from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'required': 'Email is required'})

    class Meta:
        model = User
        fields = ('email','username','password1','password2')


# class RequestEmailActivationForm(forms.Form):
