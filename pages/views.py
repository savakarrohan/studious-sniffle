from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """Home page view"""
    template_name: str = "home.html"
    