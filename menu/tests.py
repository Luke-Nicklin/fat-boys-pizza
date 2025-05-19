from django.test import TestCase
from django.db import models
from decimal import Decimal
from .models import Menu

class MenuModelTest(TestCase):

    def test_menu_creation(self):
        """Test that a Menu object can be created with the correct attributes."""
        menu_item = Menu.objects.create(
            name="Margherita Pizza",
            description="Classic pizza with tomato sauce, mozzarella, and basil.",
            price=Decimal('12.99'),  # Use Decimal for consistency
            is_available=True
        )
        self.assertEqual(menu_item.name, "Margherita Pizza")
        self.assertEqual(menu_item.description, "Classic pizza with tomato sauce, mozzarella, and basil.")
        self.assertEqual(menu_item.price, Decimal('12.99'))
        self.assertTrue(menu_item.is_available)

    def test_menu_str_representation(self):
        """Test the __str__ method of the Menu model."""
        menu_item = Menu.objects.create(name="Garlic Bread", price=Decimal('4.50'))
        self.assertEqual(str(menu_item), "Garlic Bread")

    def test_menu_default_availability(self):
        """Test that the is_available field defaults to True."""
        menu_item = Menu.objects.create(name="Pasta Carbonara", price=Decimal('15.50'))
        self.assertTrue(menu_item.is_available)

    def test_menu_can_be_unavailable(self):
        """Test that the is_available field can be set to False."""
        menu_item = Menu.objects.create(name="Special Burger", price=Decimal('18.00'), is_available=False)
        self.assertFalse(menu_item.is_available)

    def test_menu_price_is_decimal(self):
        """Test that the price field is a DecimalField."""
        menu_item = Menu.objects.create(name="Salad", price=Decimal('8.75'))
        self.assertIsInstance(menu_item.price, Decimal)