from django.urls import path 
from .views import  product_list, product_detail
from .views import  HomeView



app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products', product_list.as_view(), name='product_list'),
    path('<slug:slug>/', product_list.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail.as_view(), name='product_detail'),
]