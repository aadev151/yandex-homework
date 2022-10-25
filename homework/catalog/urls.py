from django.urls import path, re_path

from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.item_list, name='catalog-main-page'),
    re_path('^(?P<pk>([1-9][0-9]+)|[1-9])/',
            views.item_detail, name='catalog-item'),
]
