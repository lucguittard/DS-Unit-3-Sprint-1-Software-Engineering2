import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 10)

    def test_stealability_explode(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), '') #insert default string
        self.assertEqual(prod.explode(), '') #insert default string

if __name__ == '__main__':
    unittest.main()
