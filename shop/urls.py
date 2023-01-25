from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.mainpage, name='mainpage'),
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('userpage', views.userpage),
    path('aboutpage', views.aboutpage),
    path('contactpage', views.contactpage),
    path('cartpage', views.cartpage),
    ]

