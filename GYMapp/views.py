from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages
from datetime import datetime,date


def form_page(request):
    if request.method == 'GET':
        if 'LoginAuth' in request.session:
            # return render(request, 'index.html')
            return HttpResponse('Scuess')
    request.session['LoginAuth'] = ''
    return HttpResponse('Scuess')
    # return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        errors = gymUsers.objects.basic_validtor(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return HttpResponse('Scuess')
            # return redirect('/')
        Register(request)
    # return redirect('/')
    return HttpResponse('Scuess register')



def login(request):
    if request.method == "POST":
        if Login(request):
            # return redirect('/dashboard')
            return HttpResponse('Scuess login')
        else:
            # return redirect('/')
            return HttpResponse('Scuess login')
    return HttpResponse('Scuess login')


def clear(request):
    # del request.session['LoginAuth']
    # del request.session['userid']
    # return redirect('/')
    return HttpResponse('Scuess')


def dashboard(request):
    if request.method =='POST':
        pass
    now = datetime.now()
    today=now.date()
    print(today)
    # id=int(request.session['userid'])
    id=2 #gymid
    if (subScriptions.objects.filter(_to__gte=today,gymUser=id).exists()):
        list=subScriptions.objects.filter(_to__gte=today,gymUser=id)
        # print(subScriptions.objects.filter(_to__gte=today,gymUser=id)[0].participantUser.participantName)
        for user_in_gym in list:
            print(user_in_gym.participantUser.participantName)
    # return render(request,'dashboard.html',context=context)
    return HttpResponse('Scuess dashboard')