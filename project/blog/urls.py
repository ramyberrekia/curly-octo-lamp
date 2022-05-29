from django.urls import path 
from .views import (PostListView, PostDetailView, PostTagList, PostCreateView, PostUpdateView, PostDeleteView)

app_name = 'blog'


urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('create/', PostCreateView.as_view(), name='posts_create'),
    path('tags/<slug:slug>/', PostTagList.as_view(), name='posts_tag_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='posts_detail'),
    path('<slug:slug>/edit/', PostUpdateView.as_view(), name='posts_edit'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='posts_delete'),
]