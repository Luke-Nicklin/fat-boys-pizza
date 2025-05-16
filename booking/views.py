from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy, reverse
from .models import Booking
from .forms import BookingForm
from django.contrib import messages

class AddBooking(LoginRequiredMixin, CreateView):
    """
    Add a new booking.
    """

    template_name = "booking/add-booking.html"
    model = Booking
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('booking:booking-confirmed', kwargs={'pk': self.object.pk})
    

class BookingConfirmed(LoginRequiredMixin, DetailView):
    """
    Confirm the booking.
    """

    model = Booking
    template_name = "booking/booking-confirmed.html"
    context_object_name = "booking"

    def get_queryset(self):
        """
        Ensure that only the bookings of the logged-in user can be viewed.
        """
        return Booking.objects.filter(customer=self.request.user)


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
        return Booking.objects.filter(customer=self.request.user).order_by("date", "booking_time")
    

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
        If the form is valid, save the booking and redirect to the manage bookings page.
        """
        messages.success(self.request, "Booking updated successfully.")
        print("Booking updated successfully.")
        return super().form_valid(form)


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a booking.
    """

    model = Booking
    template_name = "booking/booking-confirm-delete.html"
    success_url = reverse_lazy("booking:manage-bookings")
    pk_url_kwarg = "booking_id"

    def test_func(self):
        """
        Ensure that only the user who made the booking can delete it.
        """
        return self.request.user == self.get_object().customer

    def get_queryset(self):
        """
        Ensure that only the bookings of the logged-in user can be deleted.
        """
        return Booking.objects.filter(customer=self.request.user)
    
    def form_valid(self, form):
        """
        If the form is valid, delete the booking and redirect to the manage bookings page.
        """
        messages.success(self.request, "Booking deleted successfully.")
        return super(DeleteBooking, self).form_valid(form)
