from django.urls import path
from . import views

urlpatterns = [
    path('', views.getItems),
    path('create/', views.addItem),
]