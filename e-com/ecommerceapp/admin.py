from django.contrib import admin
from .models import Contact,Product,Category,ProductRelatedImage

# Register your models here.

class ProductRelatedImageModel(admin.StackedInline):
    model = ProductRelatedImage
    
class ProductRelatedImageInline(admin.ModelAdmin):
    inlines = [ProductRelatedImageModel]

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Product,ProductRelatedImageInline)
admin.site.register(ProductRelatedImage)