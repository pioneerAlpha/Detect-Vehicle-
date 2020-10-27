from django import forms

class IndexForm(forms.Form):
    '''Image upload form.'''
    image = forms.ImageField()