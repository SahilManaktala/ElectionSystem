from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
import string
import pyqrcode

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
    person.middle_name = request.POST.get("mname", None)
    person.last_name = request.POST.get("lname", None)
    person.gender = request.POST.get('gender', None)
    person.fathers_name = request.POST.get('faname', None)
    person.mothers_name = request.POST.get('moname', None)
    person.phone_number = request.POST.get('cnumber', None)
    person.email = request.POST.get('email')
    person.pan = request.POST.get('Pan', None)
    person.housenum = request.POST.get('hnum', None)
    person.streetnum = request.POST.get('sname', None)
    person.postalnum = request.POST.get('pnum', None)
    country_id = '01'
    state_id = str(request.POST.get('state', None))
    district_id = str(request.POST.get('district', None))
    tehsil_id = str(request.POST.get('tehsil', None))
    gram_panchayat_id = str(request.POST.get('gram_panchayat', None))
    person.gram_panchayat_id = country_id + state_id + district_id + tehsil_id + gram_panchayat_id
    q = Person.objects.raw('SELECT MAX(person_id), id FROM smart_card_person WHERE gram_panchayat_id="' + person.gram_panchayat_id + '"')
    max_id = ''
    for row in q:
        max_id = row.person_id
    person.person_id = next_string(max_id)
    person.save()
    big_code = pyqrcode.create(str(person.gram_panchayat_id) + str(person.person_id), error='L', mode='binary')
    big_code.png('smart_card/static/smart_card/images/qrcode.png', scale=2, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    context = {
        'ID': person.gram_panchayat_id + person.person_id,
        'name': person.first_name + ' ' + person.middle_name + ' ' + person.last_name,
        'fathers_name': person.fathers_name,
        'gender': person.gender,
        'postalnum': person.postalnum
    }
    return render(request, 'smart_card/ID.html', context)
