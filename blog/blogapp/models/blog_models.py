from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Bashliq")
    text = models.TextField(max_length=10000, verbose_name="Metn")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaradilma Tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yenileme Tarixi")
    
    class Meta:
        verbose_name = "Blog yazisi"
        verbose_name_plural = "Blog Yazilari"
        ordering = ["-id"] 
        
    def __str__(self):
        return self.title
        