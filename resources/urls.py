from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('videos/', views.VideoListView.as_view(), name='videos'),
    path('b/<slug:slug>/', views.BookDetailView.as_view(), name='book'),
    path('v/<slug:slug>/', views.VideoDetailView.as_view(), name='video')
]