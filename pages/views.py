from django.shortcuts import render
from models import Page

def landing(request, name):
    data = {
        'data': Page.objects.get(url_string=name)
    }
    print name
    print data

    return render(request, 'landing.html', data)
