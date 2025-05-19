from django.test import TestCase
from django.contrib.auth.models import User
from .models import Table, Booking, BOOKING_TIME
from django.utils import timezone

class TableModelTest(TestCase):

    def test_table_creation(self):
        """Test that a Table object can be created with the correct attributes."""
        table = Table.objects.create(table_number=1, capacity=6)
        self.assertEqual(table.table_number, 1)
        self.assertEqual(table.capacity, 6)
        self.assertFalse(table.is_booked)

    def test_table_str_representation(self):
        """Test the __str__ method of the Table model."""
        table = Table.objects.create(table_number=2, capacity=6)
        self.assertEqual(str(table), "Table 2 - Capacity: 6")

class BookingModelTest(TestCase):

    def setUp(self):
        """Set up data for the Booking model tests."""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.table = Table.objects.create(table_number=3, capacity=6)
        self.booking_date = timezone.now().date()

    def test_booking_creation(self):
        """Test that a Booking object can be created with the correct attributes."""
        booking = Booking.objects.create(
            customer=self.user,
            name="Alice Smith",
            phone_number="01234567890",
            table=self.table,
            booking_time=2,
            date=self.booking_date,
            guests=4
        )
        self.assertEqual(booking.customer, self.user)
        self.assertEqual(booking.name, "Alice Smith")
        self.assertEqual(booking.phone_number, "01234567890")
        self.assertEqual(booking.table, self.table)
        self.assertEqual(booking.booking_time, 2)
        self.assertEqual(booking.date, self.booking_date)
        self.assertEqual(booking.guests, 4)

    def test_booking_str_representation(self):
        """Test the __str__ method of the Booking model."""
        booking = Booking.objects.create(
            customer=self.user,
            name="Bob Johnson",
            phone_number="09876543210",
            table=self.table,
            booking_time=5,
            date=self.booking_date,
            guests=2
        )
        booking_time_display = dict(BOOKING_TIME).get(5, "")
        self.assertEqual(str(booking), f"Booking for Bob Johnson on {self.booking_date} at {booking_time_display}")

