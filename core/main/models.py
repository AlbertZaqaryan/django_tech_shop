from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('Category image', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catbrand')
    name = models.CharField('Brand name', max_length=30)
    about = models.TextField('Brand about')
    img = models.ImageField('Brand image', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
