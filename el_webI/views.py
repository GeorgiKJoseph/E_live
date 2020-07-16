from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import serial
from .models import Component_data, Board, history
from .serializers import Component_status_Serializer, Status_shifter_Serializer,BoardInfoSerializer
from .forms import ComponentStatusForm

try:
    ser = serial.Serial('/dev/ttyACM0',19200,timeout=1)
except :
    print ('Connection failed: Serial port')

def home(request):
    return render(request,'el_webI/home.html',{})

def component_control(request):
    return render(request,'el_webI/com_con_tube.html',{})

def room(request):
    return render(request,'el_webI/room.html',{})

def history(request):
    return render(request,'el_webI/history.html',{})

def billpayment(request):
    return render(request,'el_webI/billpayment.html',{})

def billpredictor(request):
    return render(request,'el_webI/billpredictor.html',{})

# JSON response REST_framework
# /status
class component_status_list(APIView):

    def get(self,request,boardNo):
        #
        # getting board and device info from DB
        d1_stat = Component_data.objects.filter(boardNo=boardNo,deviceNo=1)
        d2_stat = Component_data.objects.filter(boardNo=boardNo,deviceNo=2)
        d3_stat = Component_data.objects.filter(boardNo=boardNo,deviceNo=3)
        d4_stat = Component_data.objects.filter(boardNo=boardNo,deviceNo=4)
        brd_stat = Board.objects.filter(boardNo=boardNo)
        #
        # Preparing response data
        data = {
            'd1Stat' : d1_stat[0].status,
            'd2Stat' : d2_stat[0].status,
            'd3Stat' : d3_stat[0].status,
            'd4Stat' : d4_stat[0].status,
            'instantPower' : brd_stat[0].instant_power,
            'totalPower' : 0,
        }
        #
        # Sending response
        return Response(data)

    def put(self,request):
        comp = get_object_or_404(Component_data,boardNo=1,deviceNo=1)
        serializer = Component_status_Serializer(instance=comp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class status_shifter(APIView):
    def get(self,request,boardNo,deviceNo):
        status = Component_data.objects.filter(boardNo=boardNo,deviceNo=deviceNo)
        serializer = Status_shifter_Serializer(status, many=True)
        comp_1 = get_object_or_404(Component_data,boardNo=boardNo,deviceNo=deviceNo)
        sta = ComponentStatusForm(instance=comp_1)
        #
        # Updating Database and Board
        if comp_1.status == True:
            comp_1=sta.save(commit=False)
            comp_1.status = False
            comp_1.save()
            boardControl(boardNo,deviceNo,'false')

        else:
            comp_1=sta.save(commit=False)
            comp_1.status = True
            comp_1.save()
            boardControl(boardNo,deviceNo,'true')
        return Response(serializer.data)

    def put(self,request):
        pass

#
# Arduino input JSON format
#{"InfoType":"StatusInfo","BoardNo":"1","DeviceNo":"1","Status":"true"}
def boardControl(boardNo,deviceNo,status):
    try:
        ser_cmd = '{"InfoType":"StatusInfo","BoardNo":'+str(boardNo)+',"DeviceNo":'+str(deviceNo)+',"Status":"'+status+'"}'
        ser.write(bytes(ser_cmd, encoding= 'utf-8'))
    except:
        print("Unable to connect...\nError: /dev/ttyACM0 not found")
