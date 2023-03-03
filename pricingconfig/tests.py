from django.test import TestCase
from .models import Pricing
from .utils import calculate_price

class PricingTestCase(TestCase):
    def setUp(self):
        Pricing.objects.create(base_distance=3, base_time=2, distance_base_price=80, distance_additional_price=25, time_multiplier_factor=1.33, status='Active' )

    def test_animals_can_speak(self):
        """Price calculation test"""
        pricing_config = Pricing.objects.filter(status='Active').latest('updated_at')
        self.assertEqual(calculate_price(1, 2, pricing_config), 86.45)
