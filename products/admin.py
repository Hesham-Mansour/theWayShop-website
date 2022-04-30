from django.contrib import admin
from .models import *

# Register your models here.


# Class Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','title_tag','category','is_feature','sale')
    list_display_links = ('id','image_tag','title_tag')
    list_editable = ('is_feature','sale')

class ProductAttrAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','product','price','size')
    list_display_links = ('id','image_tag','product')


# Register
admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductAttr,ProductAttrAdmin)
admin.site.register(Size)
