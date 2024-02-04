from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', views.all_users),
    path('add/', views.add),
    path('add_user/', views.add_user),
    path('detail/<int:id>/', views.detail),
    path('delete_user/<int:id>/', views.delete_user),
    path('edit/<int:id>/', views.edit),
    path('edit_user/<int:id>/', views.edit_user),
]