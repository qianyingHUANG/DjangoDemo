from django.test import TestCase

# Create your tests here.
from ProductApp.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='P1', sku='P1FR', description='P1FRDES')
        Product.objects.create(name='P2', sku='P2FR', description='P2FRDES')

    def test_product_by_name(self):
        product1 = Product.objects.get(name='P1')
        self.assertEqual(product1.sku, 'P1FR')
