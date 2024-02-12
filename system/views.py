from django.shortcuts import render
from rest_framework import generics
from datetime import date
import datetime
from .models import Product, Part, Order
from .serializers import ProductSerializer, PartSerializer, OrderSerializer

from .paginations import Pagination


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PartListCreate(generics.ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    pagination_class = Pagination


class PartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class ExpiredProducts(generics.ListAPIView):
    queryset = Part.objects.filter(expiry_date__lt=date.today())
    serializer_class = PartSerializer
    pagination_class = Pagination


class FreshProducts(generics.ListAPIView):
    queryset = Part.objects.filter(expiry_date__gt=date.today() + datetime.timedelta(days=3))
    serializer_class = PartSerializer
    pagination_class = Pagination


class ExpiringProducts(generics.ListAPIView):
    queryset = Part.objects.filter(expiry_date__gt=date.today() + datetime.timedelta(days=3)).exclude(expiry_date__lt=date.today())
    serializer_class = PartSerializer
    pagination_class = Pagination


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
