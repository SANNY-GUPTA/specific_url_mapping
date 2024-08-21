from django.urls import path
from ipl.views import * 


urlpatterns = [
    path('captain/',captain,name='captain')
]
