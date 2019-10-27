from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('on/', views.switch_on, name='switch_on'),
    path('off/',views.switch_off,name='switch_off'),
    path('component/',views.component_control,name='component_control'),
]