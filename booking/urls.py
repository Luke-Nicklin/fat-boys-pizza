from django.urls import path
from .views import AddBooking


urlpatterns = [
    path('', AddBooking.as_view(), name='add_booking'),
]