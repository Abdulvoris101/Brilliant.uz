from .views import IndexView, AboutView, ContactView, PortfolioView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]
