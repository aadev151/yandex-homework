from django.urls import path

from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='home'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item'),
]
