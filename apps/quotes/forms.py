from django import forms
from .models import post


class homeForm(forms.ModelForm):

    post = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Write a post'
                }
    ))

    class Meta:
        model = post
        fields = ('post',)
