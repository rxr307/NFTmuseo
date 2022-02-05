from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name = 'gallery_app'


urlpatterns = [
    path('newgallery/', views.newgallery, name='newgallery'),
    path('editgallery/', views.editgallery, name='editgallery'),
]