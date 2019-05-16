from django.urls import path, reverse
from .views import HomePageView, FlavorDetailView, CreateNewView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('icecream/<int:pk>/', FlavorDetailView.as_view(), name='flavor_detail'),
    path('flavor/new/', CreateNewView.as_view(), name='create_view')
]