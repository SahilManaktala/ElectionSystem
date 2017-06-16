from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
import string

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

def next_string(current):
    l = [str(i) for i in range(0, 10)]
    l = l + list(string.ascii_uppercase)
    s = list(current)
    i = len(current) - 1
    ch = l[(l.index(s[i]) + 1) % 36]
    while i != -1:
        s[i] = ch
        if ch != '0':
            break
        i = i - 1
        ch = l[(l.index(s[i]) + 1) % 36]
    return ''.join(s)

def do_register(request):
    person = Person()
    person.first_name = request.POST.get("fname", None)
    person.last_name = request.POST.get("lname", None)
    person.gender = request.POST.get('gender', None)
    person.fathers_name = request.POST.get('faname', None)
    person.mothers_name = request.POST.get('moname', None)
    person.phone_number = request.POST.get('cnumber', None)
    person.email = request.POST.get('email')
    person.pan = request.POST.get('Pan', None)
    country_id = '1'
    state_id = str(request.POST.get('state', None))
    district_id = str(request.POST.get('district', None))
    tehsil_id = str(request.POST.get('tehsil', None))
    gram_panchayat_id = str(request.POST.get('gram_panchayat', None))
    person.gram_panchayat_id = country_id + state_id + district_id + tehsil_id + gram_panchayat_id
    person.address = request.POST.get('address', None)
    q = Person.objects.raw('SELECT MAX(person_id), id FROM smart_card_person WHERE gram_panchayat_id="' + person.gram_panchayat_id + '"')
    max_id = ''
    for row in q:
        max_id = row.person_id
    person.person_id = next_string(max_id)
    person.save()
    #return HttpResponse(person.gram_panchayat_id + person.person_id)
    context = {
        'ID': person.gram_panchayat_id + person.person_id
    }
    return render(request, 'smart_card/do_register.html', context)