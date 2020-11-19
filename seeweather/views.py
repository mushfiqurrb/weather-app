from django.shortcuts import render
import json
import requests

# Create your views here.

def home(request):

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=11&API_KEY=EA32BBFE-2E20-4266-8C97-961EBBCA8A0D")

    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "ERRORRR..."


    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})
