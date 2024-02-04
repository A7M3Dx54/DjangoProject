from django.contrib import admin
from django.urls import path, include
from subtasks import views

urlpatterns = [
    path('detail/<int:id>/', views.sub_detail),
    path('add/<int:id>', views.add),
    path('delete_subtask/<int:id>/', views.delete_subtask),
    path('edit/<int:id>/', views.edit),
    path('edit_subtask/<int:id>/', views.edit_subtask),
    path('', admin.site.urls),
    
]