from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Booking
from .forms import BookingForm


class AddBooking(LoginRequiredMixin, CreateView):
    """
    View to handle the creation of a new booking.
    """
    template_name = 'booking/add-booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/booking/success/'

    def form_valid(self, form):
        """
        If the form is valid, save the booking and redirect to the success page.
        """
        form.instance.customer = self.request.customer
        return super(AddBooking, self).form_valid(form)