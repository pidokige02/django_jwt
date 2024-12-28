# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['email'].label = "Email Address"
        self.fields['email'].help_text = "Please provide a valid email address."
        self.fields['password1'].help_text = "Password must be at least 8 characters long."

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_at']  # 수정 가능한 필드