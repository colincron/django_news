from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# Create your views here.

def get_weather():
        r = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=27.7920&lon=82.7239&exclude=minutely,hourly,daily,alerts&units=imperial&appid=c587510ed59d1b940a70fea012677a36")
        data = r.json()
        temp = data['current']['temp']
        return temp

class HomePageView(TemplateView):
    template_name = 'home.html'
    current_weather = get_weather()
