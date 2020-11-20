from django.shortcuts import render
import json
import requests

# Create your views here.

def home(request):

    if request.method=="POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zipcode+"&date=2020-11-20&distance=30&API_KEY=EA32BBFE-2E20-4266-8C97-961EBBCA8A0D")

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "ERRORRR..."

        if api[0]['Category']['Name'] == 'Good':
            category_color = 'good'
        elif api[0]['Category']['Name'] == 'Moderate':
            category_color = 'moderate'
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
            category_color = 'usg'
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_color = 'unhealthy'
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_color = 'veryunhealthy'
        elif api[0]['Category']['Name'] == 'Hazardous':
            category_color = 'hazardous'

        return render(request, 'home.html', {'api':api,'category_color':category_color})
    
    else:
        api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20002&date=2020-11-20&distance=30&API_KEY=EA32BBFE-2E20-4266-8C97-961EBBCA8A0D")

        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "ERRORRR..."

        if api[0]['Category']['Name'] == 'Good':
            category_color = 'good'
        elif api[0]['Category']['Name'] == 'Moderate':
            category_color = 'moderate'
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
            category_color = 'usg'
        elif api[0]['Category']['Name'] == 'Unhealthy':
            category_color = 'unhealthy'
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            category_color = 'veryunhealthy'
        elif api[0]['Category']['Name'] == 'Hazardous':
            category_color = 'hazardous'

        return render(request, 'home.html', {'api':api,'category_color':category_color})

def about(request):
    return render(request, 'about.html', {})
