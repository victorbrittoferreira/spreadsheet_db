from django.contrib import admin
from core import models
# Register your models here.


@admin.register(models.Planilha)
class PlanilhaAdmin(admin.ModelAdmin):
    list_display = ["external_key", "client_name", "created", "updated"]
    search_fields = ["client_name", "external_key"]
    list_filter = ["client_name"]
