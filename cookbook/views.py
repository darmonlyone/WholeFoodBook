from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def menu(request):
    return render(request, 'menu.html')
