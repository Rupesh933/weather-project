from django.shortcuts import render
from .utils import get_weather

def index(request):
    # Handle weather search from and display current weather
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            data = get_weather(city)
            if data:
                # extract only needed fields for the templates
                weather_data = {
                    'city' : data['name'],
                    'country' : data['sys']['country'],
                    'tempreature' : data['main']['temp'],
                    'feel_like' : data['main']['feel_like'],
                    'humidity' : data['main']['humidity'],
                    'pressure' : data['main']['pressure'],
                    'wind_speed' : data['wind']['speed'],
                    'description' : data['weather']['description'],
                    'icon' : data['weather'][0]['icon']
                }
            else:
                error_message = f"Could not find weather city '{city}', Check city name and try again!"
        else:
            error_message = 'Please enter a city name'
    context = {
        'weather' : weather_data,
        'error' : error_message
    }
    return render(request, 'index.html', context)