from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import MyModel

class MyView(ListView):
    template_name = 'list.html'
    model = MyModel
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context