from django.urls import path
from . import views

app_name = 'ajax_frontend'

urlpatterns = [
    path('', views.my_list, name='my_list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
