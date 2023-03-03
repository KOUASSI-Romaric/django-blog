from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:id_article>', views.detail, name='detail')
]
