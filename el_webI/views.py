from django.shortcuts import render
import serial

#ser = serial.Serial('/dev/ttyACM0',9800,timeout=1)
# Create your views here.
def home(request):
    return render(request,'el_webI/home.html',{})

def switch_on(request):
    #ser.write(b'H')
    return render(request,'el_webI/switch_on.html',{})

def switch_off(request):
    #ser.write(b'L')
    return render(request,'el_webI/switch_off.html',{})

def component_control(request):
    return render(request,'el_webI/component_control.html',{})