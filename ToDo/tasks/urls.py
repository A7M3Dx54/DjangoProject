from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('detail/<int:id>/', views.detail),
    path('add/', views.add),
    path('add_task/', views.add_task),
    path('delete_task/<int:id>/', views.delete_task),
    path('edit/<int:id>/', views.edit),
    path('edit_task/<int:id>/', views.edit_task),
    path('', admin.site.urls),
    
]