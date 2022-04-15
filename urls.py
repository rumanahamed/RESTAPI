from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('post/',views.Product_Detail.as_view()),
    path('get/',views.Product_list_view.as_view()),
    path('ProductDetailView/<pk>/',views.Product_detail_view.as_view()),
]
