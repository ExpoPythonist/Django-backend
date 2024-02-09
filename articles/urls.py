from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ArticleListView.as_view(), name='article-list'),
    path('create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
