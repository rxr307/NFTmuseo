
from logging import Filter
from django.contrib import auth
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .models import NewGallery, NewNFT, User
from .forms import NewGalleryForm, FilterForm
from django.contrib.auth import (authenticate, get_user_model,
login as django_login,
logout as django_logout )
from django.contrib.auth.decorators import login_required
import requests
import json
from datetime import datetime, tzinfo
from django import template
from django.utils.safestring import mark_safe



# def newgallery(request, username):


@login_required
def creategallery(request, username):

    if request.method == 'GET':
            
        form = NewGalleryForm()
        
        context = {
        'form': form,
        'username': username,
        }

        return render(request, 'galleries/newgallery.html', context)

    if request.method == "POST":
    
        form = NewGalleryForm(request.POST)

        if form.is_valid():
            new_gallery = form.save(commit = False)
            ## connect the new gallery with the user (foreign key)
            new_gallery.user = request.user        
            new_gallery.save()
            url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=49"

            params={'owner': new_gallery.wallett_address}
            headers = {
                "Accept": "application/json",
                "X-API-KEY": "78c06f9034b74f4a8a115600360b47f9"
            }
            response = requests.request("GET", url, headers=headers, params=params)
            response = response.json()["assets"]

            list_of_nfts =  []
            for dictionary in response:
                token_id = dictionary["token_id"]
                token_address = dictionary["asset_contract"]["address"]
                contract_address = 'https://api.opensea.io/api/v1/asset/' + token_address + '/' + token_id + '/'
                name = dictionary["name"]
                if name is not None and len(name) > 50:
                    name = (name[:50] + '...')
                nft_created_date = dictionary["asset_contract"]["created_date"]
                nft_created_date = nft_created_date[:10]
                nft_created_date = datetime.strptime(nft_created_date, '%Y-%m-%d').strftime('%m/%d/%Y')
                image = dictionary["image_url"]
                description = dictionary["description"]
                if description is not None and '*' in description:
                    head, sep, tail = description.partition('*')
                    description = head
                if description is not None and len(description) > 50:
                    description = (description[:150] + '...')
                if isinstance(description, str) != True:
                    description = 'No description provided'
                link = dictionary["permalink"]
                nft_dict = {
                'contract_address': contract_address,
                'name': name,
                'image': image,
                'description': description,
                'link': link,
                'nft_created_date': nft_created_date,
                }
                list_of_nfts.append(nft_dict)

            print(new_gallery.id)

            context = {
            'gallery_id': new_gallery.id, 
            'new_gallery': new_gallery,
            'list_of_nfts': list_of_nfts,
            'raw_nft_data': json.dumps(list_of_nfts),
            'new_gallery_name': new_gallery.gallery_name,
            'user': new_gallery.user,
            username:username,
        
            }
 
          
            return render(request, 'galleries/editgallery.html', context )
  


@login_required
def galleryview(request, username, gallery_id):

    if request.method == 'GET':
            
        gallery = NewGallery.objects.get(id=gallery_id)
        list_of_saved_nfts = NewNFT.objects.filter(gallery=gallery.id)

        context = {
        'list_of_saved_nfts': list_of_saved_nfts,
        'gallery': gallery,
        'username': username,
        }

        return render(request, 'galleries/galleryview.html', context)

    if request.method == "POST":
        save_list = request.POST.getlist('include')
        nft_dicts = request.POST['nft_list']
        print(type(nft_dicts))
        nft_dicts = nft_dicts.replace("'", '"')
        nft_dicts = json.loads(nft_dicts)
        
        saved_nft_dicts = []
        for dict in nft_dicts: 
            if dict['contract_address'] in save_list:        
                new_nft = NewNFT.objects.create(
                description = dict['description'],
                name = dict['name'],
                image = dict['image'],
                link = dict['link'],
                nft_created_date = dict['nft_created_date'],
                gallery = NewGallery.objects.get(id=gallery_id),
                user = request.user,
                )
                new_nft.save()
                saved_nft_dicts.append(dict)

        if saved_nft_dicts == []:
            gallery = NewGallery.objects.get(id=gallery_id)
            list_of_saved_nfts = NewNFT.objects.filter(gallery=gallery.id)

            context = {
            'new_gallery': gallery,
            'username': username,
            'user': gallery.user,            
            'errors': ['Please select at least 1 NFT'],
            'list_of_nfts': nft_dicts,
            'new_gallery_name': gallery.gallery_name,
            }
            return render(request, 'galleries/editgallery.html', context)

        else:
                
            list_of_saved_nfts = []
            for dict in saved_nft_dicts: 
                description = dict['description'],
                name = dict['name'],
                image = dict['image'],
                link = dict['link'],
                nft_created_date = dict['nft_created_date'],
                list_of_saved_nfts.append(dict)
            
            

            gallery = NewGallery.objects.get(id=gallery_id)
    
            context = {
                'gallery': gallery,
                'username': username,
                'list_of_saved_nfts': list_of_saved_nfts,
                'user': username,
                
            }
            
            return render(request, 'galleries/galleryview.html', context)

@login_required
def museumview(request):

    if request.method == 'GET':
            
        public_galleries = NewGallery.objects.filter(public_gallery=True).order_by('-created_date')

        list_of_public_galleries = []
        for gallery in public_galleries:
            if gallery.newnft.count() > 0:
                list_of_public_galleries.append(gallery)
       
        form = FilterForm()
        
        context = {
            'list_of_public_galleries': list_of_public_galleries,
            'form': form,
        }
        

        return render(request, 'galleries/museumview.html', context)

@login_required
def filteredmuseum(request):

    if request.method == 'POST':

        form = FilterForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data
            category = category['filter_museum']
  
       
     
        filtered_galleries = NewGallery.objects.filter(public_gallery=True, gallery_category=category).order_by('-created_date')

        list_of_filtered_galleries = []
        for gallery in filtered_galleries:
            if gallery.newnft.count() > 0:
                list_of_filtered_galleries.append(gallery)
        
        print(list_of_filtered_galleries)
       

        context = {
            'list_of_public_galleries': list_of_filtered_galleries,
            'form': form,
        }
        
        return render(request, 'galleries/museumview.html', context)


@login_required
def delete(request, pk):
    deleted_item = get_object_or_404(NewGallery, pk=pk)
    deleted_item.delete()
  
    return redirect(reverse('users_app:userprofile', args=[request.user.username]))

@login_required
def delete_nft(request, pk):
    
    deleted_item = get_object_or_404(NewNFT, pk=pk)
    deleted_item.delete()

  
    return redirect(reverse('users_app:userprofile', args=[request.user.username]))

@login_required
def gallerylike(request, gallery_id):
 
    print('hello')

    gallery_obj = get_object_or_404(NewGallery, id=gallery_id)
    
    this_user = request.user 

    if this_user not in gallery_obj.gallery_like.all():
        gallery_obj.gallery_like.add(this_user)

    else:
        gallery_obj.gallery_like.remove(this_user)

    print(gallery_obj.gallery_like.all())
    print(gallery_obj.gallery_like.count())


       
    return JsonResponse({
        'userliked': this_user in gallery_obj.gallery_like.all(),
        'numberlikes': gallery_obj.gallery_like.count(),
    })


        