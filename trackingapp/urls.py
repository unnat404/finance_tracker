from django.contrib import admin
from django.urls import path
from .views import stockPicker, stockTracker
urlpatterns = [
    path('', stockPicker, name = "stockpicker"),
    path('stocktracker/', stockTracker, name = "stocktracker"),    
]