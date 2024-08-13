from django.urls import path
from quality_managements.views import home 

urlpatterns = [
    path('', home)
]
