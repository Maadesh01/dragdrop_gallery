from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads_testing/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=255, blank=True) 
    def __str__(self):
        return str(self.image)
