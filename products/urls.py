from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('products/<int:id>/',views.productDetails,name='product_details'),
    path('category-product-list/<str:title>/<int:cat_id>/',views.category_product_list,name='category_product_list'),
    path('cart/',views.addCart,name='cart'),
    path('category/',views.category,name='category'),
    path('checkout/',views.checkout,name='checkout'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('my-account/',views.accountPage,name='my_account'),
    path('our-service/',views.service,name='our_service'),
    path('contact-us/',views.contactUs,name='contact_us'),
    # --------------------------- #
    path('nav',views.base,name='nav')
]
