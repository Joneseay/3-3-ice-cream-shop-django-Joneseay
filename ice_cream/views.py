from django.views.generic import ListView, DetailView
from .models import IceCream

class HomePageView(ListView):
    model = IceCream
    template_name = 'home.html'

class FlavorPageView(ListView):
    model = IceCream
    template_name = 'flavor_page.html'

class DailyPageView(ListView):
    model = IceCream
    template_name = 'daily_page.html'

class WeeklyPageView(ListView):
    model = IceCream
    template_name = 'weekly_page.html'

class SeasonalPageView(ListView):
    model = IceCream
    template_name = 'seasonal_page.html'

# Create your views here.
