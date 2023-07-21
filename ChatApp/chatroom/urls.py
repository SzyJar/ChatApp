from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('clear/<slug:slug>/', views.clear_room, name='clear_room'),
]