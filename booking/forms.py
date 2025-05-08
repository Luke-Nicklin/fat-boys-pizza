from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    """
    Form to handle booking creation.
    """
    class Meta:
        model = Booking
        fields = ['name', 'phone_number', 'table', 'booking_time', 'date', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(),
            'table': forms.Select(),
            'guests': forms.NumberInput(attrs={'min': 1}),
        }


