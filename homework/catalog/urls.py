from django.urls import path, re_path

from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.item_list, name='home'),
    path('<int:pk>/', views.item_detail, name='item'),
]
