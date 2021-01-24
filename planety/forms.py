from django import forms
from django.contrib.auth.models import User
from . models import Profile, Post, Comment

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','Dob','image','cover_photos']



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class videoform(forms.ModelForm):
    class Mete:
        model = Post
        fields = ('video', 'caption')