from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def index(request):
    return render(request, 'smart_card/index.html', context=None)

def register(request):
    context = {
        'sta' : State.objects.all()
    }

    return render(request, 'smart_card/register.html', context)

def details(request):
    return render(request, 'smart_card/details.html', context=None)



def get_districts(request):
    state_id = request.GET.get('state_id', None)
    data = District.objects.filter(state_id = str(state_id))
    result = []
    for row in data:
        info = {}
        info['district_id'] = row.district_id
        info['district_name'] = row.district_name
        result.append(info)
    return JsonResponse(result, safe = False)

def get_tehsils(request):
    country_id = request.GET.get('country_id', None)
    state_id = request.GET.get('state_id', None)
    district_id = request.GET.get('district_id', None)
    parent_id = str(country_id) + str(state_id) + str(district_id)
    data = Tehsil.objects.filter(district_id = parent_id)
    result = []
    for row in data:
        info = {}
        info['tehsil_id'] = row.tehsil_id
        info['tehsil_name'] = row.tehsil_name
        result.append(info)
    return JsonResponse(result, safe = False)

def get_gram_panchayats(request):
    country_id = request.GET.get('country_id', None)
    state_id = request.GET.get('state_id', None)
    district_id = request.GET.get('district_id', None)
    tehsil_id = request.GET.get('tehsil_id', None)
    parent_id = str(country_id) + str(state_id) + str(district_id) + str(tehsil_id)
    data = GramPanchayat.objects.filter(tehsil_id = parent_id)
    result = []
    for row in data:
        info = {}
        info['gram_panchayat_id'] = row.gram_panchayat_id
        info['gram_panchayat_name'] = row.gram_panchayat_name
        result.append(info)
    return JsonResponse(result, safe = False)