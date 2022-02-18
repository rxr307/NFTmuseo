from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name = 'gallery_app'


urlpatterns = [
    # path('newgallery/<str:username>/', views.newgallery, name='newgallery'),
    path('creategallery/<str:username>/', views.creategallery, name='creategallery'),
    path('galleryview/<str:username>/<int:gallery_id>/', views.galleryview, name='galleryview'),
    path('museumview/', views.museumview, name='museumview'),
    path('filteredmuseumview/', views.filteredmuseum, name='filteredmuseumview'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('deletenft/<int:pk>/', views.delete_nft, name='deletenft'),
    path('like/<int:gallery_id>', views.gallerylike, name='gallerylike')
]