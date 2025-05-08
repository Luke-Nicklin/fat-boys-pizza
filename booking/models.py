from django.db import models
from django.contrib.auth.models import User



# Capacity and booking time
CAPACITY = ((6, "6"))
BOOKING_TIME = ((1, "12:00pm - 1:15pm"), (2, "1:30pm - 2:45pm"), (3, "3:00pm - 4:15pm"), (4, "4:30pm - 5:45pm"), (5, "6:00pm - 7:15pm"))


class Table(models.Model):
    """
    Table model to represent a table in the restaurant.
    """
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=CAPACITY, default=6)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.table_number} - Capacity: {self.capacity}"


class Booking(models.Model):
    """
    Booking model to represent a booking made by a customer.
    """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='booking_customer')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='booking_table')
    booking_time = models.IntegerField(choices=BOOKING_TIME, default=1)
    date = models.DateField()

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.booking_time}"
    
