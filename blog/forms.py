from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='maksymalnie 200 znaków')


    class Meta:
        model = Post
        fields = ['title', 'text', 'image']


# Klasa Meta przekazuje Django informacje o tym jaki model powinien
# być wykorzystany do stworzenia tego formualarza
# oraz jakie pola powinny pojawić się w formularzu
