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
            'description': SummernoteWidget(attrs={'summernote': {'width': '430px', 'height': '450px'}}),
            'ingredients': SummernoteWidget(attrs={'summernote': {'width': '430px', 'height': '450px'}}),
            'preparation': SummernoteWidget(attrs={'summernote': {'width': '430px', 'height': '450px'}}),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields[
            'title'
            ].label = ""

