from django import forms
from django.db.models import fields
from .models import NewGallery, NewNFT, User 

# class NewNFTForm(forms.ModelForm):

#     #meta describes data used to make form, which fields, widgets, database model

#     class Meta: 

#         #this form is for the User model 
#         model = NewNFT

#         fields = [
#             'NFT_name',
#             'caption',
#             'price',
#             'link',
#             'image',
          
#         ]

#         widgets = {
#             'NFT_name': forms.TextInput(attrs={'class':'form-control'}),
#             'caption': forms.Textarea(attrs={'class':'form-control'}),
#             'price': forms.TextInput(attrs={'class':'form-control'}),
#             'link': forms.TextInput(attrs={'class':'form-control'}),
#             'image': forms.FileInput(attrs={'class':'form-control'}),
#         }

# class NewNFTFormOpenSea(forms.ModelForm):
    
#     #meta describes data used to make form, which fields, widgets, database model

#     class Meta: 

#         #this form is for the User model 
#         model = NewNFT

#         fields = [
#             'contract_address',
#             'token_id',
       
#         ]

#         widgets = {
#             'contract_address': forms.TextInput(attrs={'class':'form-control'}),
#             'token_id': forms.TextInput(attrs={'class':'form-control'}),
    
#         }


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

