from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, reverse

from core.models import Planilha
from core.forms.planilha import PlanilhaForm

import json
import pandas as pd
import datetime


def list_details_xls(request, id):

    try:
        xls = Planilha.objects.get(id=id)
        xls_file = xls.file
        df = pd.DataFrame(pd.read_excel(xls_file, header=0, index_col=False))
        df = df.to_dict("split")

        Region = 0
        BuidingId = 1
        CostCentre = 2
        TelcoCode = 3
        BuildingCurrentUse = 4
        Country = 5
        LocalCurrencyName = 6
        CostDate = 7
        BudFXRate = 8
        RentLCY = 9
        UtilitiesLCY = 10
        FacilityLCY = 11
        SuppliesLCY = 12

        lista = []
        for x in df['data']:

            entry = {
                'Region': x[Region],
                'BuidingId': x[BuidingId],
                'CostCentre': x[CostCentre],
                'TelcoCode':  x[TelcoCode],
                'BuildingCurrentUse': x[BuildingCurrentUse],
                'Country': x[Country],
                'LocalCurrencyName': x[LocalCurrencyName],
                'CostDate': str(x[CostDate]),
                'BudFXRate': x[BudFXRate],
                'RentLCY':  x[RentLCY],
                'UtilitiesLCY': x[UtilitiesLCY],
                'FacilityLCY': x[FacilityLCY],
                'SuppliesLCY': x[SuppliesLCY],
            }
            lista.append(entry)

        context = {'context': lista}
        return render(request, "planilha/planilha_details.html", context)
    except:
        return redirect(reverse('error'))


def add_xls(request):

    try:
        if request.POST:
            form = PlanilhaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                new_planilha = Planilha.objects.last()
                xls_file = new_planilha.file
                df = pd.read_excel(xls_file)
                df = pd.DataFrame(pd.read_excel(
                    xls_file, header=0, index_col=False))
                df = df.to_dict("split")
                my_xls_data = json.dumps(df, default=str)
                new_planilha.data = my_xls_data
                new_planilha.save()
                messages.add_message(
                    request, messages.SUCCESS, "Planilha created with success!"
                )

                return redirect(reverse('list-all-xls'))

        else:
            form = PlanilhaForm()

        context = {
            "title": "Add Planilha",
            "active": "planilha",
            "form": form,
        }

        return render(request, "planilha/get_planilha.html", context)
    except:
        return redirect(reverse('error'))


def list_all_xls(request):

    lista = []
    if request.method == "POST":
        # pdb.set_trace()
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        search_result = Planilha.objects.filter(
            created__date__range=(fromdate, todate))

        for p in search_result:

            lista.append(
                {
                    "id": p.pk,
                    "created_at": p.created,
                    "external_key": p.external_key,
                    "client_name": p.client_name,
                    "file": p.file,
                    "data": p.data,
                }
            )

        context = {"planilha": lista, "title": 'Planilhas'}
        return render(request, "planilha/planilha_list.html", context)

    else:
        planilhas = Planilha.objects.all()
        for p in planilhas:
            lista.append(
                {
                    "id": p.pk,
                    "created_at": p.created,
                    "external_key": p.external_key,
                    "client_name": p.client_name,
                    "file": p.file,
                    "data": p.data,
                }
            )

        context = {"planilha": lista, "title": 'Planilhas'}

        return render(request, "planilha/planilha_list.html", context)


# --------------------------------------------------------------


def delete_xls(request, id):
    try:
        xls = Planilha.objects.get(id=id)
        xls.delete()
        return redirect(reverse('list-all-xls'))
    except:
        return redirect(reverse('error'))


def error(request):
    context = {
    }
    return render(request, "planilha/error.html", context)
