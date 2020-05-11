from django import forms
from post_questions.models import Post, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'questions']


# widget = {
#    'title': forms.TextInput(attrs={'class': 'textinputclass'}),
# }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


#        widget = {
#           'title': forms.TextInput(attrs={'class': 'textinputclass'}),
#      }


form = QuestionForm()
