from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import serial
from .models import Component_status, Component_data, home, history
from .serializers import Component_status_Serializer

#ser = serial.Serial('/dev/ttyACM0',9800,timeout=1)
# Create your views here.
def home(request):
    return render(request,'el_webI/home.html',{})

def switch_on(request,pk):
    #ser.write(b'H')
    status_data = get_object_or_404(Component_status, pk=pk)
    
    return render(request,'el_webI/switch_on.html',{})

def switch_off(request):
    #ser.write(b'L')
    return render(request,'el_webI/switch_off.html',{})

def component_control(request):
    return render(request,'el_webI/component_control.html',{})

# JSON response REST_framework
# /status
class component_status_list(APIView):

    def get(self,request):
        status = Component_status.objects.all()
        serializer = Component_status_Serializer(status, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass