from django.urls import path 
from .views import HotelListView, HotelDetailView, HotelCreateView

app_name = 'hotels'

urlpatterns = [
    path('', HotelListView.as_view(), name='hotels_list'),
    path('new/', HotelCreateView.as_view(), name='hotels_create'),
    path('<slug:slug>/', HotelDetailView.as_view(), name='hotels_detail'),
]