from django.contrib import admin
from .models import Component_status, Component_data, home, history

admin.site.register(Component_status)
admin.site.register(Component_data)
admin.site.register(home)
admin.site.register(history)
