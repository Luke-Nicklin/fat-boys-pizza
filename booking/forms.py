from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    """
    Form to handle booking creation.
    """
    class Meta:
        model = Booking
        fields = ['customer', 'name', 'phone_number', 'table', 
                  'booking_time', 'date', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'table': forms.Select(),
            'booking_time': forms.Select(),
            'guests': forms.NumberInput(attrs={'min': 1}),
        }


