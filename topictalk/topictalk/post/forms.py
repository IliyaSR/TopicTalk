from django import forms
from topictalk.post.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['choose_community', 'post_title', 'post_content', 'image']
        widgets = {
            'post_title': forms.TextInput(attrs={'placeholder': 'Post Title', 'class': 'border-widget'}),
            'post_content': forms.Textarea(attrs={"size": 10})
        }
        labels = {
            'post_title': "Post Title",
            'post_content': 'Post Content'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'id': 'comment'})
        }

        labels = {
            'text': 'Your Comment:'
        }
