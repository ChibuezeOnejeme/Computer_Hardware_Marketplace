from django.contrib.auth.models import User
from django.db import models
from PIL import Image
# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=255)
   
   # this class if for name amendedment
    class Meta:
        ordering =('name',)
        verbose_name_plural ='Categories'
   
   # To show the saved object name we have to invoke the string representation

    def __str__(self):

      return self.name
    
class Item(models.Model):
   #linking category to items
   category =models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
   name = models.CharField(max_length=255)
   description =models.TextField(blank=True,null=True)
   price = models.FloatField()
   image = models.ImageField(upload_to='uploads',blank=True,null=True)
   is_sold =models.BooleanField(default=False)
   #linking creators to the item
   created_by =models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
   created_at =models.DateTimeField(auto_now_add=True)

   # To show the saved object name we have to invoke the string representation

   def __str__(self):

      return self.name
   
   def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 100 or img.width > 100:
           output_size = (500, 500)
           img.thumbnail(output_size)
           img.save(self.image.path)