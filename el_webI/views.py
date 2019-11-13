from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import serial
from .models import Component_status, Component_data, home, history
from .serializers import Component_status_Serializer, Status_shifter_Serializer
from .forms import ComponentStatusForm
try:
    ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
except :
    print ('Connection failed!')
# Create your views here.
def home(request):
    return render(request,'el_webI/home.html',{})

def switch_on(request):
    try:
        comp_1 = get_object_or_404(Component_status,pk=1)
        sta = ComponentStatusForm(instance=comp_1)
        comp_1=sta.save(commit=False)
        comp_1.status = False
        comp_1.save()
        ser.write(b'H')
    except:
        print ('Connection failed!')
    #status_data = get_object_or_404(Component_status, pk=pk)
    return render(request,'el_webI/switch_on.html',{})

def switch_off(request):
    try:
        comp_1 = get_object_or_404(Component_status,pk=1)
        sta = ComponentStatusForm(instance=comp_1)
        comp_1=sta.save(commit=False)
        comp_1.status = True
        comp_1.save()
        ser.write(b'L')
    except:
        print ('Connection failed!')
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
    
    def put(self,request):
        comp = get_object_or_404(Component_status,pk=1)
        serializer = Component_status_Serializer(instance=comp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class status_shifter(APIView):
    def get(self,request):
        status = Component_status.objects.all()
        serializer = Status_shifter_Serializer(status, many=True)
        comp_1 = get_object_or_404(Component_status,pk=1)
        sta = ComponentStatusForm(instance=comp_1)
        if comp_1.status == True:
            try:
                comp_1=sta.save(commit=False)
                comp_1.status = False
                comp_1.save()
                ser.write(b'H')
            except:
                print ('Connection failed!')
        elif comp_1.status == False:
            try:
                comp_1=sta.save(commit=False)
                comp_1.status = True
                comp_1.save()
                ser.write(b'L')
            except:
                print ('Connection failed!')                   

        return Response(serializer.data)
    def put(self,request):
        pass