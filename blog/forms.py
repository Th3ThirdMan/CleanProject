from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields[
            'body'
            ].label = ""


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'ingredients', 'preparation')

        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'preparation': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields[
            'title'
            ].label = ""
