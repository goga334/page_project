from django.urls import path
from .views import HomePageView, PhotoPageView

urlpatterns = [
    path('photo/', PhotoPageView.as_view(), name='photo'),
    path('', HomePageView.as_view(), name='home'),
]
