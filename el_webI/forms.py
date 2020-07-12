from django import forms
from .models import Component_data

class ComponentStatusForm(forms.ModelForm):

    class Meta:
        model = Component_data
        fields = ('deviceNo', 'status')
