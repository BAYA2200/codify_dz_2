from django.contrib import admin
from django.urls import path

from credit import views

urlpatterns = [
    path('list/', views.ClientListView.as_view(), name='list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='detail'),

]