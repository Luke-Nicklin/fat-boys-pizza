from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    """
    Form to handle booking creation.
    """

    class Meta:
        model = Booking
        fields = [
            "customer",
            "name",
            "phone_number",
            "table",
            "booking_time",
            "date",
            "guests",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "table": forms.Select(),
            "booking_time": forms.Select(),
            "guests": forms.NumberInput(attrs={"min": 1}),
        }

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < timezone.now().date():
            raise ValidationError("Booking date cannot be in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get("table")
        date = cleaned_data.get("date")
        booking_time = cleaned_data.get("booking_time")

        if table and date and booking_time:
            # Check if a booking already exists for this table, date, and time
            if Booking.objects.filter(table=table, date=date, booking_time=booking_time).exists():
                raise ValidationError(
                    "This table is already booked on this date at this time."
                )
        return cleaned_data