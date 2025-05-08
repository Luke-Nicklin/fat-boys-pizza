from django.views.generic import CreateView

from .models import Booking
from .forms import BookingForm


class AddBooking(CreateView):
    """
    View to handle the creation of a new booking.
    """
    template_name = 'booking/add_booking.html'
    model = Booking
    form_class = BookingForm
    fields = ['name', 'phone_number', 'table', 'booking_time', 'date', 'guests']
    success_url = '/booking/success/'  # Redirect to a success page after booking

    def form_valid(self, form):
        """
        If the form is valid, save the booking and redirect to the success page.
        """
        form.instance.customer = self.request.customer
        return super(AddBooking, self).form_valid(form)