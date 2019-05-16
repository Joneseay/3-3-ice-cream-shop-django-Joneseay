from django.views.generic import ListView, DetailView, CreateView
from .models import IceCream

class HomePageView(ListView):
    model = IceCream
    template_name = 'home.html'


class FlavorDetailView(DetailView):
    model = IceCream
    template_name = 'flavor_detail.html'

class CreateNewView(CreateView):
    model = IceCream
    template_name = 'flavor_new.html'
    fields = ['flavor', 'base', 'available', 'featured', 'date']