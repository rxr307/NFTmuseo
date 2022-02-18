from django import forms
from django.db.models import fields
from .models import NewGallery, NewNFT, User 


CATEGORY_CHOICES = (
    ('animal','ANIMAL'),
    ('music', 'MUSIC'),
    ('cinema','CINEMA'),
    ('abstract','ABSTRACT'),
    ('architecture','ARCHITECTURE'),
    ('colletibles', 'COLLECTIBLES'),
    ('utility', 'UTILITY'),
    ('photography', 'PHOTOGRAPHY'),
    ('virtual-world', 'VIRTUAL-WORLD'),
    ('various', 'VARIOUS'), 
)

class NewGalleryForm(forms.ModelForm):
    
    #meta describes data used to make form, which fields, widgets, database model

    class Meta: 

        #this form is for the User model 
        model = NewGallery

        

        fields = [
            'public_gallery',
            'gallery_name',
            'gallery_category',
            'wallett_address',
        ]

        widgets = {
            'gallery_name': forms.TextInput(attrs={'class':'form-control'}),
            'wallett_address': forms.TextInput(attrs={'class':'form-control'}),
            'public_gallery': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'gallery_category': forms.Select(attrs={'class':'form-select'}),
        }

class FilterForm(forms.Form):

    

    CATEGORY_CHOICES = (
    ('animal','ANIMAL'),
    ('music', 'MUSIC'),
    ('cinema','CINEMA'),
    ('abstract','ABSTRACT'),
    ('architecture','ARCHITECTURE'),
    ('colletibles', 'COLLECTIBLES'),
    ('utility', 'UTILITY'),
    ('photography', 'PHOTOGRAPHY'),
    ('virtual-world', 'VIRTUAL-WORLD'),
    ('various', 'VARIOUS'), 
)
    filter_museum = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-select'}))
    
    fields = [
        'filter_museum'
    ]