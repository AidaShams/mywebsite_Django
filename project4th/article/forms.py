from django import forms
# from django.forms import widgets, fields
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comment',
            'writer',
            'article'
        )
        widgets = {
            "article": forms.HiddenInput(),
            "writer": forms.HiddenInput()
        }