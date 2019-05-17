from django.views.generic import ListView, DetailView, CreateView
from .models import IceCream

class HomePageView(ListView):
    model = IceCream
    template_name = 'home.html'

    queryset = IceCream.objects.filter(featured = True)


class FlavorDetailView(DetailView):
    model = IceCream
    template_name = 'flavor_detail.html'


class CreateNewView(CreateView):
    model = IceCream
    template_name = 'flavor_new.html'
    fields = ['flavor', 'base', 'available', 'featured', 'date']


class SelectFlavorView(ListView):
    model = IceCream
    template_name = 'menu_select.html'

    def get_queryset(self):
        selection = self.kwargs['available'].upper()

        if selection == 'ALL':
            return IceCream.objects.all()
        else:
            return IceCream.objects.filter( available = selection)

