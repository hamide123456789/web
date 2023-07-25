from django.urls import path
from .import views


app_name = 'home'
urlpatterns = [
    path('',views.invoice_list,name='home'),
    path('invoice/detail/<int:pk>/', views.invoice_detail.as_view(), name='invoice_detail'),
    path('create_view/', views.create_view, name='create_view'),
    path('update/<int:pk>/', views.invoice_update_view , name='invoice_update_view'),
    path('delete_view/<int:pk>/', views.delete_view, name='delete_view'),
    path('my_view/',views.my_view, name='my_view'),
    path('product',views.product_list,name='product'),
    path('product/details/<int:pk>/', views.product_detail.as_view(), name='product_detail'),
    path('product/create_view/', views.product_create_view, name='product_create_view'),
    path('product/update/<int:pk>/', views.product_update_view , name='product_update_view'),
    path('product/delete_view/<int:pk>/', views.product_delete_view, name='product_delete_view'),
    path('product/my_view/',views.product_my_view, name='product_my_view'),


]