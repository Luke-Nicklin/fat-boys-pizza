from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuListView.as_view(), name='menu'),
]
