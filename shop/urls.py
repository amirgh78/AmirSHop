from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('mainpage/', views.mainpage, name='mainpage'),
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('userpage', views.userpage),
    path('aboutpage', views.aboutpage),
    path('contactpage', views.contactpage),
    path('cartpage', views.cartpage),
    path('mainpage', views.mainpage),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    ]

