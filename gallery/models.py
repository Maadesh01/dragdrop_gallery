from django.db import models

class Post(models.Model):
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} - {self.uploaded_at}"

class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads_testing/')
    order = models.IntegerField(default=0)  # To maintain image order in slideshow

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image {self.id} for Post {self.post.id}"
