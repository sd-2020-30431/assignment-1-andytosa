from django.urls import path
from .views import (
    FoodListView,
    FoodCreateView,
    ExpiredListView
)
from . import views

urlpatterns = [
    path('', views.home, name='core-home'),
    path('myfood/<str:username>', FoodListView.as_view(), name='myfood'),
    path('expired/<str:username>', ExpiredListView.as_view(), name='expired'),
    path('new/', FoodCreateView.as_view(), name='add-food'),  
]