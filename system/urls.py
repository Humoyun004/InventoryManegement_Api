from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('part/', views.PartListCreate.as_view(), name='part_list'),
    path('parts/<int:pk>/', views.PartDetail.as_view(), name='part_detail'),
    path("expired/", views.ExpiredProducts.as_view(), name="expired"),
    path("fresh/", views.FreshProducts.as_view(), name="fresh"),
    path("expiring/", views.ExpiringProducts.as_view(), name="expiring"),
    path("orders/", views.OrderList.as_view(), name="order_list"),
]