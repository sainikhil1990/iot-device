from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, 'iot_app/home.html')
def userlogin(request):
    return render(request, 'iot_app/userlogin.html')
def logindata(request):
    user_name = request.POST.get('uname')
    password = request.POST.get('pwd')
    if user_name == 'admin' and password == '1111':
        request.session['user_name'] = user_name
        return render(request, "iot_app/dashboard.html",{"data": models.device_info.objects.all()})
    else:
        return HttpResponse("Invalid login details")
def  logout(request):
     try:
        del request.session['user_name']
     except:
        pass
     return redirect('/')
def getlogindata(request):
    user_name = request.POST.get('uname')
    password = request.POST.get('pwd')
    #user = auth.authenticate(request, user_name=user_name, password=password)
    if models.user_logindetails.objects.filter(user_name=user_name, password = password):
        request.session['user_name'] = user_name
        return HttpResponse(user_name + " Logged in successfully")
    else:
        return HttpResponse("invalid username or password")


def signup(request):
    return render(request, 'iot_app/signup.html')
def getuserdata(request):
    user_name = request.POST.get('uname')
    password = request.POST.get('pwd')
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    dept = request.POST.get('dept')
    auth_level = request.POST.get('auth_level')
    email_id = request.POST.get('email_id')
    info = [first_name, last_name,age,address,email_id]
    if models.user_logindetails.objects.filter(user_name =user_name):
        return HttpResponse('Username exists')
    else:
        obj1 , created = models.user_logindetails.objects.get_or_create(user_name= user_name, password=password)
    obj1.save()
    obj = models.user_info(first_name=first_name, last_name=last_name, dept=dept,auth_level=auth_level,email_id=email_id)
    obj.save()
    return render(request, "iot_app/userlogin.html")

import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@require_http_methods(["POST"])
def dashboard(request):
    if request.session.has_key('user_name'):
        return render(request, 'iot_app/dashboard.html')
    else:
        return render(request, 'iot_app/notfound.html')

@csrf_exempt
@require_http_methods(["POST"])
def device_info(request):
    if request.body:
        data = json.loads(request.body.decode('utf-8'))

        print(data)
        out1 = data['temp'].replace("\\r\\n'",'')
        out = out1[2:]

        obj2 = models.device_info(device_id = data['id'],
                                  device_name = data['name'],
                                  temp = data['temp'],
                                  date = data['date_time'])
        obj2.save()

        rowlist = len(models.device_info.objects.all())
        if rowlist > 40:
           delete_row = models.device_info.objects.filter(id=406).delete()
        print(rowlist)
        return HttpResponse("OK")
    else:
        info = {"response":"data not found",
                "status":"400"}
        return HttpResponse(json.dumps(info))
#def sensorUI(request):
    #return render(request, 'iot_app/dashboard.html', {"data": models.device_info.objects.all()})
@csrf_exempt
@require_http_methods(["POST"])

def get_sensordata(request):
    if request.body:
        data = json.loads(request.body.decode('utf-8'))
        obj1 = models.Sensor1(name = data['Sensor1']['name'],
                                  Value=data['Sensor1']['Value'],
                                  Desc=data['Sensor1']['Desc'],
                                  time_stamp=data['time_stamp'])

        obj2 = models.Sensor2(name=data['Sensor2']['name'],
                              Value=data['Sensor2']['Value'],
                              Desc=data['Sensor2']['Desc'],
                              time_stamp=data['time_stamp'])
        obj3 = models.Sensor3(name=data['Sensor3']['name'],
                              Value=data['Sensor3']['Value'],
                              Desc=data['Sensor3']['Desc'],
                              time_stamp=data['time_stamp'])
        obj1.save()
        obj2.save()
        obj3.save()
        print(data)
        return HttpResponse("OK")
    else:
         info = {"response": "data not found",
            "status": "400"}
         return HttpResponse(json.dumps(info))

def sensor1_ui(request):
    return render(request, 'iot_app/sensor1.html', {"data": models.Sensor1.objects.all()})
def sensor2_ui(request):
    return render(request, 'iot_app/sensor2.html', {"data": models.Sensor2.objects.all()})
def sensor3_ui(request):
    return render(request, 'iot_app/sensor3.html', {"data": models.Sensor3.objects.all()})

def sensor_dashboard(request):
    return render(request, 'iot_app/sensor_dashboard.html')
@csrf_exempt
@require_http_methods(["POST"])

def controloutput(request):
    value = request.POST.get('name')

    #if id == 1:
    d = {"name" :"LED",
    "value" : "1"}
    encode_data = json.dumps(d).encode('utf-8')
    r = http.request('POST',
                        'http://192.168.29.8:8000/set_led',
                        body=encode_data,
                        headers={'Content-Type': 'application/json'}
                     )
    return HttpResponse("ON")

