from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #path('on/', views.switch_on, name='switch_on'),
    #path('off/',views.switch_off,name='switch_off'),
    path('component/',views.component_control,name='component_control'),
    path('room/',views.room,name='room'),
    path('history/',views.history,name='history'),
    path('billpayment/',views.billpayment,name='billpayment'),
    path('billpredictor/',views.billpredictor,name='billpredictor'),
    #path('respjson/',views.respjson,name='respjson'),
    url(r'^status/(?P<boardNo>\d+)/$', views.component_status_list.as_view()),
    url(r'^statusshifter/(?P<boardNo>\d+)/(?P<deviceNo>\d+)/$', views.status_shifter.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
