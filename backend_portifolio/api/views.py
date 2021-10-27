from django.shortcuts import render, redirect, reverse
from core.models import Planilha

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import PlanilhaSerializer


class PlanilhaListAPI(APIView):

    def get(self, request):

        planilha = Planilha.objects.all()
        serializer = PlanilhaSerializer(planilha, many=True)

        return Response(serializer.data)


class PlanilhaDetailAPI(APIView):

    def get_object(self, id):
        planilha = get_object_or_404(Planilha, id=id)
        return planilha

    def get(self, request, id):

        try:
            planilha = Planilha.objects.get(id=id)
            serializer = PlanilhaSerializer(planilha)

            return Response(serializer.data)

        except:
            return redirect(reverse('error'))


class PlanilhaDeleteAPI(APIView):

    def get_object(self, id):
        planilha = get_object_or_404(Planilha, id=id)
        return planilha

    def get(self, request, id):

        try:
            planilha = Planilha.objects.get(id=id)
            planilha.delete()

            return redirect(reverse('api-planilha-list'))

        except:
            return redirect(reverse('error'))


class PlanilhaListDate(APIView):

    def get(self, request):
        # import pdb
        # pdb.set_trace()
        date = request.GET.get('date')

        planilha = Planilha.objects.filter(created__date=date)

        serializer = PlanilhaSerializer(planilha, many=True)

        return Response(serializer.data)


class PlanilhaListRange(APIView):

    def get(self, request):
        # import pdb
        # pdb.set_trace()
        date_beg = request.GET.get('date_beg')
        date_end = request.GET.get('date_end')

        print(date_beg)
        print(date_end)

        planilha = Planilha.objects.filter(
            created__date__range=(date_beg, date_end))
        serializer = PlanilhaSerializer(planilha, many=True)

        return Response(serializer.data)
