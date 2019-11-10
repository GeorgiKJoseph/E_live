from django import forms
from .models import Component_status

class ComponentStatusForm(forms.ModelForm):

    class Meta:
        model = Component_status
        fields = ('cid', 'status')