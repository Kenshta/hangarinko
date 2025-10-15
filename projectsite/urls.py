from django.contrib import admin
from django.urls import path
from hangapp.views import HomePageView
from hangapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
]