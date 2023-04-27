
from django.urls import path
from .class_view import HomeView, MovieList, MovieCreate, MovieDetail, MovieUpdate, MovieDelete

"""
urlpatterns = [
    path('', MovieList.as_view(), name='home'),
    path('<int:pk>', MovieDetail.as_view(), name='detail'),
    path('add', MovieCreate.as_view(), name='add'),
    path('edit/<int:pk>', MovieUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', MovieDelete.as_view(), name='delete'),
]
"""

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movies/', MovieList.as_view(), name='index'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='detail'),
    path('movies/add/', MovieCreate.as_view(), name='add'),
    path('movies/<int:pk>/edit', MovieUpdate.as_view(), name='edit'),
    path('movies/<int:pk>/delete', MovieDelete.as_view(), name='delete'),
]