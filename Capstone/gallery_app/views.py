
from django.contrib import auth
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import NewGalleryForm
from django.contrib.auth import (authenticate, get_user_model,
login as django_login,
logout as django_logout )
from django.contrib.auth.decorators import login_required
import requests
import json


@login_required
def newgallery(request, username):

    if request.method == 'GET':
            
        form = NewGalleryForm
        
        context = {
        'form': form,
        'username': username,
        }

        return render(request, 'galleries/newgallery.html', context)

    elif request.method == "POST":
    
        form = NewGalleryForm(request.POST)

        if form.is_valid():

            new_gallery = form.save(commit = False)
            
            ## connect the new gallery with the user (foreign key)
            new_gallery.user = request.user
            
            new_gallery.save()

            url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=15"


            # params={'owner': '0x81c587eb0fe773404c42c1d2666b5f557c470eed'}

            headers = {
                "Accept": "application/json",
                "X-API-KEY": "78c06f9034b74f4a8a115600360b47f9"
            }

            response = requests.request("GET", url, headers=headers)

            response = response.json()["assets"]

            list_of_urls =  []

            for dictionary in response:
                token_id = dictionary["token_id"]
                token_address = dictionary["asset_contract"]["address"]
                asset_url = 'https://api.opensea.io/api/v1/asset/' + token_address + '/' + token_id + '/'
                list_of_urls.append(asset_url)

            list_of_images = []

            for url in list_of_urls:
                response = requests.request("GET", url, headers=headers) 
                response = response.json()
                response = response['image_url']
                list_of_images.append(response)

            list_of_names = []

            for url in list_of_urls:
                response = requests.request("GET", url, headers=headers) 
                response = response.json()
                response = response['name']
                list_of_names.append(response)
             

            context = {
            'new_gallery_name':new_gallery.gallery_name,
            'list_of_images':list_of_images,
            'list_of_names':list_of_names,
            }

            return render(request, 'galleries/editgallery.html', context)
  



@login_required
def editgallery(request, username):

    context = {
    'username': username,
    }

    

    return render(request, 'galleries/editgallery.html', context)





























# @login_required
# def nftcard(request):
 
#     if request.method == 'GET':
        
#             form = NewNFTForm
#             form2 = NewNFTFormOpenSea

#             context = {
#             'form': form,
#             'form2': form2,
#             }

#             return render(request, 'galleries/nftcard.html', context)

#     elif request.method == "POST":

#             form = NewNFTForm(request.POST)

#             if form.is_valid():
                    
#                 new_nft = form.save(commit = False)
                
#                 ## connect the new nft with the gallery (foreign key)
#                 new_nft.gallery = request.gallery
                
#                 new_nft.save()


#                 return render(request, 'galleries/nftcard.html')