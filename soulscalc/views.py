from django.utils import timezone
from django.views.generic import ListView, FormView

from .models import *


# Create your views here.
class GamesView(ListView):
    model = Games
    template_name = 'soulscalc/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class CalculatorView(FormView):
    form_class = Calculator
    template_name = 'soulscalc/calculator.html'

    def form_valid(self, form):
        form.__str__()
        return super().form_valid(form)
