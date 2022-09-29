from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Credentials
from django.shortcuts import redirect


def index(request):
    template = loader.get_template('Login.html')
    context = {
        'test': request.session.get('flag', -1),
    }
    return HttpResponse(template.render(context, request))


def check(request):
    user = request.POST['user']
    pwd = request.POST['pwd']
    creds = Credentials.objects.all().values()
    request.session['flag'] = 0
    for x in creds:
        if x['username'] == user:
            if x['password'] == pwd:
                request.session['flag'] = 2
                break
            else:
                request.session['flag'] = 1
                break
    if request.session['flag'] == 2:
        template = loader.get_template('DashBoard.html')
        context = {
            'id': user,
        }
        return HttpResponse(template.render(context, request))
    return HttpResponseRedirect(reverse('index'))


def new_user(request):
    template = loader.get_template('NewUser.html')
    return HttpResponse(template.render({}, request))


def add_user(request):
    x = request.POST['user']
    y = request.POST['pwd']
    request.session['flag'] = -1
    cred = Credentials(username=x, password=y)
    cred.save()
    return HttpResponseRedirect(reverse('index'))
