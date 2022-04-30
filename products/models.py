from django.db import models
from django.utils.html import format_html

# Create your models here.


# Main Category
class MainCategory(models.Model) :
    title = models.CharField(("title   "), max_length=100)

    class Meta :
        verbose_name = ("Main Category")
        verbose_name_plural = ("MainCategorys")

    def __str__(self): 
        return self.title


# Category
class Category(models.Model) :
    title = models.CharField(("title   "), max_length=100)
    image = models.ImageField(("Image   "), upload_to="product_img/")
    m_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    class Meta :
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self) :
        return self.title


# Size
class Size(models.Model) :
    title = models.CharField(("Size "), max_length=50)

    class Meta :
        verbose_name = ("Size")
        verbose_name_plural = ("Sizes")

    def __str__(self) :
        return self.title


# Product
class Product(models.Model): 
    title = models.CharField(("title   "), max_length=200)
    details = models.TextField(("Details   "))
    count = models.IntegerField(("Count in store"))
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    img_1 = models.ImageField(("Image 1   "), upload_to="product_img/")
    img_2 = models.ImageField(("Image 2   "), upload_to="product_img/")
    img_3 = models.ImageField(("Image 3   "), upload_to="product_img/")
    is_feature = models.BooleanField(("Is Featured   "))
    sale = models.BooleanField(("Sale   "))

    def image_tag(self):
        return format_html('<img src="{}" width="50px" height="50px">', self.img_1.url)
    

    def title_tag(self):
        return format_html("<h5 style='font-size:14px; fontwieght:bold;'>{}</h5>", self.title)

    def __str__(self) :
        return self.title


# Product Attributes
class ProductAttr(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    old_Price = models.IntegerField(("Des Price   "))
    price = models.IntegerField(("Price "))
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    image = models.ImageField(("Image   "), upload_to="product_img/")


    def image_tag(self):
        return format_html('<img src="{}" width="50px" height="50px">', self.image.url)

    class Meta :
        verbose_name = ("ProductAttr")
        verbose_name_plural = ("ProductAttrs")

    def __str__(self) :
        return self.product.title
