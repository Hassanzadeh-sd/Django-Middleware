from django.shortcuts import render, HttpResponse


def Home(request):
    print("Home Page View")
    return HttpResponse("Home Page")
