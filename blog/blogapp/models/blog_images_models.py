from django.db import models

from .blog_models import Blog

class BlogImagesModel(models.Model):
    """
    Represents an image associated with a blog post.

    Attributes:
        blog (ForeignKey): The blog post this image belongs to.
        image (ImageField): The image file, optional.
        created_at (DateTimeField): Timestamp when the image was created.
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(verbose_name="Blog Shekili", blank=True, null=True, upload_to="blog_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.blog.title} - {self.created_at}"