from django.views.generic import ListView

from .models import Menu


class MenuListView(ListView):
    """
    View to display the list of menu items.
    """
    model = Menu
    template_name = 'menu/menu.html'
    context_object_name = 'menu'

    def get_queryset(self):
        """
        Optionally filter the menu items based on availability.
        """
        return Menu.objects.filter(is_available=True)
