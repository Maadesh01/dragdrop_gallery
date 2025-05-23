from django.shortcuts import render, redirect
from .models import UploadedImage

def upload_images(request):
    if request.method == 'POST':
        caption = request.POST.get('caption', '')  # 👈 Get caption
        for image in request.FILES.getlist('images'):
            UploadedImage.objects.create(image=image, caption=caption)
        return render(request, 'gallery/upload.html', {'success': True})
    return render(request, 'gallery/upload.html')

def gallery(request):
    images = UploadedImage.objects.all().order_by('uploaded_at')
    print("Images count:", images.count())
    return render(request, 'gallery/gallery.html', {'images': images})
