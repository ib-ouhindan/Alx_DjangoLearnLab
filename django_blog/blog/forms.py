from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget()
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
     widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your content here...'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
