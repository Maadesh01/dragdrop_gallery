from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('upload/', views.upload_images, name='upload'),
    path('gallery/', views.gallery, name='gallery'),
]
