from django.urls import path 
from .views import activation_failed

app_name = 'accounts'


urlpatterns = [
    path('activation_failed/',activation_failed,name='activation_failed')
]