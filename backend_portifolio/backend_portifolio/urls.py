from django.contrib import admin
from django.urls import path


     # Import functions 
from api.views import PlanilhaListAPI, PlanilhaDetailAPI, PlanilhaDeleteAPI, PlanilhaListDate, PlanilhaListRange
from core.views import list_all_xls, list_details_xls, add_xls, delete_xls, error



urlpatterns = [

     # Core Urls
    path('', list_all_xls, name='list-all-xls'),
    path('admin/', admin.site.urls),
    path('list-all-xls/', list_all_xls, name='list-all-xls'),
    path('list-details-xls/<int:id>', list_details_xls, name='list-details-xls'),

    path('add-xls', add_xls, name='add-xls'),
    path('delete-xls/<int:id>', delete_xls, name='delete-xls'),

    # Api Urls
    path("api/list_planilhas", 
          PlanilhaListAPI.as_view(), name="api-planilha-list"),

    path("api/list-details-xls/<int:id>",
         PlanilhaDetailAPI.as_view(), name="api-planilha-details"),
         
    path("api/delete-planilha/<int:id>",
         PlanilhaDeleteAPI.as_view(), name="api-delete-planilha"),
    
                
    # List all planilhas by date
    path("api/list_planilhas_by_date", PlanilhaListDate.as_view(),
         name="api-list-planilha-date"),

    # List all planilhas by range
    path("api/list_planilhas_by_range", PlanilhaListRange.as_view(),
         name="api-list-planilha-range"),






    # Error Handling
    path('error/', error, name='error'),

    # To do list:
    #   Refactor
    #       2- Optimize and Create some Methods.
    #       3- Try to OOP this code as much as I can.
]
