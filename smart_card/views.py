from django.shortcuts import render

def index(request):
    return render(request, 'smart_card/index.html', context=None)
