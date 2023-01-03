from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.product_list, name='product_list'),
]

urlpatterns += staticfiles_urlpatterns()
