"""Taotao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from manager import views

urlpatterns = [
    path('index', views.index),
    path('item/add', views.ItemController.additem),
    path('item/list', views.ItemController.getitemlist),
    path('item/save', views.ItemController.additem),
    path('item/param/list', views.ItemController.getitembyid),
    path('content', views.ContentController.getcontent),
    path('content/category/list', views.ContentCategoryController.getcontentcategorylist),
    path('content/category/update', views.ContentCategoryController.updatecontentcategory),
    path('content/category/create', views.ContentCategoryController.createcontentcategory),
    path('content/category/delete', views.ContentCategoryController.deletecontentcategory)
]
