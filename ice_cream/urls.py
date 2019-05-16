from django.urls import path
from .views import HomePageView, FlavorPageView, DailyPageView, WeeklyPageView, SeasonalPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('icecream/<int:pk>/', FlavorPageView.as_view(), name = 'flavor_page'),
    path('icecream/<int:pk>/', DailyPageView.as_view(), name = 'daily_page'),
    path('icecream/<int:pk>/', WeeklyPageView.as_view(), name = 'weekly_page'),
    path('icecream/<int:pk>/', SeasonalPageView.as_view(), name = 'seasonal_page'),
]
