from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('on/', views.switch_on, name='switch_on'),
    path('off/',views.switch_off,name='switch_off'),
    path('component/',views.component_control,name='component_control'),

    #path('respjson/',views.respjson,name='respjson'),
    url(r'^status/', views.component_status_list.as_view()),
    url(r'^statusshifter/', views.status_shifter.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)