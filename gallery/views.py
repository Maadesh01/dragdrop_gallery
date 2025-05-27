from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from .models import Post, Image
from .forms import ImageUploadForm

@csrf_exempt
def upload_images(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(caption=form.cleaned_data['caption'])
            images = request.FILES.getlist('images')
            for index, image in enumerate(images):
                Image.objects.create(
                    post=post,
                    image=image,
                    order=index
                )
            return redirect('gallery:gallery')
        else:
            print("Form errors:", form.errors)
    else:
        form = ImageUploadForm()
    posts = Post.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/upload.html', {
        'form': form,
        'posts': posts,
    })

def gallery(request):
    posts = Post.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/gallery.html', {'posts': posts})

def delete_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        post.delete()
    return redirect('gallery:upload')


