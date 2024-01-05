from django import forms
from django.forms.widgets import Select
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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Add 'id' attribute to the choose_community field
            self.fields['choose_community'].widget = Select(attrs={
                'id': 'custom-sidebar',
                # Add more attributes as needed
            })



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
