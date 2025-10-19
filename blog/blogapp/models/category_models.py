from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kateqoriya")
    
    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
        ordering = ["-id"]
        
    def __str__(self):
        return self.name