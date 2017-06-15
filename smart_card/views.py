from django.shortcuts import render

def index(request):
    return render(request, 'smart_card/index.html', context=None)

def register(request):
    return render(request, 'smart_card/register.html', context=None)
