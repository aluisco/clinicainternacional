from django.urls import path
from .views import *
app_name = 'resultadoscovid'
urlpatterns = [
    path('', ResultadosCovidListView.as_view(), name='index'),
    path('import/', import_xlsx, name='import'),
    path('estadistica/', estadistica, name='estadistica'),
]

