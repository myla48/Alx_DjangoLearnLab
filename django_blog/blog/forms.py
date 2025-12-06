from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget   # 👈 import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]   # 👈 include tags field
        widgets = {
            "tags": TagWidget(),               # 👈 use TagWidget for better tag input
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
