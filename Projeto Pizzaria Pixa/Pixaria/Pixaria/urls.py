from django.contrib import admin
from django.urls import path, include

from pizzaria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('pizzas/', views.pizzas, name = 'pizzas'),
    path('restaurantes/', views.restaurantes, name = 'restaurantes'),
]
