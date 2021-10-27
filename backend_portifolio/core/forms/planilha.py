from django.forms import ModelForm
from core.models import Planilha
from django import forms


class PlanilhaForm(ModelForm):
    class Meta:
        model = Planilha
        fields = ['external_key', 'client_name', 'file']
