from django import forms
from django.contrib.auth.models import User
from .models import Posts,Blog

class loginform(forms.Form):
    email=forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class addpostform(forms.ModelForm):
    
    class Meta:
        model=Posts
        fields=('title','url','description',)


class addblogform(forms.ModelForm):
    
    class Meta:
        model=Blog
        fields=('blogtitle','content',)


class signupform(forms.ModelForm):
    pass

    class Meta:
        model = User
        fields=['first_name','last_name','password','email',]
        # exclude=('')

        # email = forms.EmailField(max_length = 256,label = 'Email')
        # first_name = forms.CharField(max_length = 30)
        # last_name=forms.CharField(max_length = 30)
        # password = forms.CharField(label='Password', widget=forms.PasswordInput())

    