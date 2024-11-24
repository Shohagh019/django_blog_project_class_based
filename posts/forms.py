from django import forms
from .models import Post, Comment
class postForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']        
