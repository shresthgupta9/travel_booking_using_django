from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tandc/', views.tandc, name='tandc'),
    path('support/', views.support, name='support'),
    path('feedback/', views.feedback, name='feedback'),
    path('book/', views.book, name='book'),
]
