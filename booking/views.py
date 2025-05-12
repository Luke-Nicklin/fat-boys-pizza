from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm


class AddBooking(LoginRequiredMixin, CreateView):
    """
    Add a new booking.
    """

    template_name = "booking/add-booking.html"
    model = Booking
    form_class = BookingForm
    success_url = "/booking/success/"

    def form_valid(self, form):
        """
        If the form is valid, save the booking and redirect to the success page.
        """
        form.instance.customer = self.request.user
        return super().form_valid(form)


class BookingList(LoginRequiredMixin, ListView):
    """
    List all bookings for the logged-in user.
    """

    model = Booking
    template_name = "booking/manage-bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        """
        Ensure that only the bookings of the logged-in user can be viewed.
        """
        return Booking.objects.filter(customer=self.request.user)


class BookingDetail(LoginRequiredMixin, DetailView):
    """
    View the details of a booking.
    """

    model = Booking
    template_name = "booking/manage-bookings.html"
    context_object_name = "booking"

    def get_queryset(self):
        """
        Ensure that only the bookings of the logged-in user can be viewed.
        """
        return Booking.objects.filter(customer=self.request.user)

class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a booking.
    """

    model = Booking
    form_class = BookingForm
    template_name = "booking/edit-booking.html"
    success_url = "/booking/manage-bookings/"
    pk_url_kwarg = "booking_id"

    def get_queryset(self):
        """
        Ensure that only the bookings of the logged-in user can be edited.
        """
        return Booking.objects.filter(customer=self.request.user)

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.customer

    def form_valid(self, form):
        """
        If the form is valid, save the booking and redirect to the success page.
        """
        return super().form_valid(form)


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a booking.
    """

    model = Booking
    template_name = "booking/booking-confirm-delete.html"
    success_url = "/booking/booking-confirm-delete.html/"

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_queryset(self):
        """
        Ensure that only the bookings of the logged-in user can be deleted.
        """
        return Booking.objects.filter(customer=self.request.user)
