from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from datetime import date, timedelta
from django.urls import reverse

from .models import Product


class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {'name': 'Test Product', 'manufacturer': 'Test Manufacturer'}
        self.response = self.client.post(reverse('product_list'), self.product_data, format='json')

    def test_create_product(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_product_list(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PartAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Test Product', manufacturer='Test Manufacturer')
        self.part_data = {'product': self.product.id, 'units': 10, 'date_produced': date.today(), 'expiry_date': date.today() + timedelta(days=3), 'total': 10}
        self.response = self.client.post(reverse('part_list'), self.part_data, format='json')

    def test_create_part(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_part_list(self):
        response = self.client.get(reverse('part_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_order_list(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

