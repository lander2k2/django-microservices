import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import Service


def home(request):
    services = Service.objects.all()
    return render(request, 'microservices/index.html', locals())


def services(request):
    services = Service.objects.all()

    response = {}
    for svc in services:
        response[svc.name] = 'http://{}'.format(svc.url)

    return HttpResponse(json.dumps(response), content_type='application/json')

