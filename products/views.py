from turtle import title
from unicodedata import category
from django.shortcuts import render
from .models import *

# Create your views here.


# base
def base(request, title):
    category = Category.objects.get(title=title)
    main_cate = MainCategory.objects.all()
    return render(request, 'navbar.html', {'category': category, 'main_cate': main_cate})


# Home Page
def home(request):
    category = Category.objects.all()[:3]
    product = Product.objects.all().order_by('id')
    return render(request, 'home.html', {'category': category, 'product': product})


# about Page
def about(request):
    return render(request, 'about.html')


# products Page
def products(request):
    data = Product.objects.all().order_by('id')
    return render(request, 'products.html', {'data': data})

# Product Details Page


def productDetails(request, id):
    data = Product.objects.get(id=id)
    product = Product.objects.all().order_by('id')
    return render(request, 'product_details.html', {'data': data, 'product': product})


# Acording to Category product list
def category_product_list(request, title, cat_id):
    cate = Category.objects.get(id=cat_id)
    cat_title = Category.objects.get(title=title)
    data = Product.objects.filter(category=cate)
    return render(request, 'category_product_list.html', {'data': data, 'cat_title': cat_title})


# Category Page
def category(request):
    data = Category.objects.all()
    return render(request, 'shop\category.html',{'data':data})


# cart Page
def addCart(request):
    return render(request, 'shop\cart.html')


# checkout Page
def checkout(request):
    return render(request, 'shop\checkout.html')


# wishlist Page
def wishlist(request):
    return render(request, 'shop\wishlist.html')


# My Account Page
def accountPage(request):
    return render(request, 'shop\myAccount.html')


# Contact Us Page
def contactUs(request):
    return render(request, 'contactUs.html')


# Service Page
def service(request):
    return render(request, 'ourService.html')


# Search Page
def search(request):
    q = request.GET['q']
    data = Product.objects.filter(title__icontains=q)
    return render(request, 'search.html', {'data': data})
