from .views import IndexView, AboutView, ContactView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
