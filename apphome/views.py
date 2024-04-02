from django.utils import timezone
from django.views.generic import ListView

from .models import Tools


# Create your views here.
class HomeView(ListView):
    model = Tools
    template_name = 'apphome/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
