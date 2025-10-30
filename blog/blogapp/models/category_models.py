from django.db import models


class Category(models.Model):
    """
    Represents a category for blog posts.

    Attributes:
        name (CharField): The name of the category.
    
    Meta:
        verbose_name: Singular name for admin display.
        verbose_name_plural: Plural name for admin display.
        ordering: Default ordering by descending id.
    """
    name = models.CharField(max_length=50, verbose_name="Kateqoriya")
    
    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
        ordering = ["-id"]
        
    def __str__(self):
        return self.name