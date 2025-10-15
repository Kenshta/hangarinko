from django.contrib import admin
from django.urls import path
from hangapp.views import HomePageView, CategoryList, CategoryCreateView, CategoryUpdateView
from hangapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('category_list', CategoryList.as_view(), name='category-list'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>',CategoryUpdateView.as_view(), name='category-update'),
]