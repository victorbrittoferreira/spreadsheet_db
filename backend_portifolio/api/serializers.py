from rest_framework import serializers
from core.models import Planilha


class PlanilhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planilha
        fields = "__all__"
