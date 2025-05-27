from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('upload/', views.upload_images, name='upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post')
]

