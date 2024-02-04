from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home_view, name='home'),
    path('tasks/', include('tasks.urls')),
    path('users/', include('accounts.urls')),
    path('subtasks/', include('subtasks.urls')),

]