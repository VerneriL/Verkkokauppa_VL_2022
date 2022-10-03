from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from users.models import FeedBack


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class FeedBackForm(forms.ModelForm):

    class Meta:
        model = FeedBack
        fields = ('fb_field',)
        labels = {
            'fb_field': '',
        }
        widgets = {
            'fb_field': forms.Textarea(attrs={'style': 'resize: none;'})
        }