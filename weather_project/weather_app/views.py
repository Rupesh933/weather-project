from django.shortcuts import render
from .utils import get_weather

def index(request):
    # Handle weather search from and display current weather
    weather_data = None
    error_message = None