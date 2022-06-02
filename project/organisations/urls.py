from django.urls import path 
from .views import OrganisationPostView, OragnisationListView, organisation_detail_view

app_name = 'organisations'

urlpatterns = [
    path('', OragnisationListView.as_view(), name='organisations_list'),
    path('post_request/', OrganisationPostView.as_view(), name='organisations_create'),
    path('<slug:slug>/', organisation_detail_view, name='organisations_detail'),
]