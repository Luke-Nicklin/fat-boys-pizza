from django.views.generic import TemplateView

class Index(TemplateView):
    """Index view"""
    template_name = "home/index.html"