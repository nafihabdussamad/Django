from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
    path('new_user/', views.new_user, name='new_user'),
    path('new_user/signup/', views.add_user, name='add_user'),
]
