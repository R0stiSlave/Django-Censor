from django.urls import path
from .views import PostList, NewsDetailView

urlpatterns = [
    path('', PostList.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]