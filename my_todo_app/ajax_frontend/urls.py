from django.urls import path
from . import views

app_name = 'ajax_frontend'

urlpatterns = [
    path('', views.my_list, name='my_list'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
