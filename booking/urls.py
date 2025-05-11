from django.urls import path
from .views import (
    AddBooking,
    BookingDetail,
    DeleteBooking,
    BookingList,
    EditBooking,
)

app_name = 'booking'

urlpatterns = [
    path("add-booking/", AddBooking.as_view(), name="add-booking"),
    path(
        "manage-bookings/",
        BookingList.as_view(),
        name="manage-bookings",
    ),
    path(
        "<int:pk>/",
        BookingDetail.as_view(),
        name="booking-detail",
    ),
    path(
        "delete/<int:booking_id>",
        DeleteBooking.as_view(),
        name="booking-confirm-delete",
    ),
    path(
        "edit/<int:booking_id>",
        EditBooking.as_view(),
        name="edit-booking",
    )
]
