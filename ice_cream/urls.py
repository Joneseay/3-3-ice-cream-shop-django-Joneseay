from django.urls import path
from .views import HomePageView, FlavorDetailView, CreateNewView, SelectFlavorView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('icecream/<int:pk>/', FlavorDetailView.as_view(), name='flavor_detail'),
    path('icecream/<available>/', SelectFlavorView.as_view(), name='selection'),
    path('flavor/new/', CreateNewView.as_view(), name='create_view'),

]