from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField()
    desc=models.TextField(max_length=50)
    phonenumber=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique =True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_product')
    # sub_category = models.CharField(max_length = 50, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length = 300)
    image = models.ImageField(upload_to = 'images/images')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
class ProductRelatedImage(models.Model):
    related_img = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'related_product_image')
    image = models.ImageField(upload_to='product_related_images', blank=True, null=True)