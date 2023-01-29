from django.shortcuts import render, redirect

from django.contrib import messages



def call_home(request):


    return render(request,"base.html")


def call_about(request):

    return render(request,"about.html")

def call_pricing(request):

    return render(request,"pricing.html")

def call_login(request):

    return render(request,"login.html")

