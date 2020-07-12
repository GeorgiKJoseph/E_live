from django.contrib import admin
from .models import Component_data, Board, history,Device_Log_24hr,Board_Log_24hr

admin.site.register(Component_data)
admin.site.register(Board)
admin.site.register(history)
admin.site.register(Device_Log_24hr)
admin.site.register(Board_Log_24hr)
