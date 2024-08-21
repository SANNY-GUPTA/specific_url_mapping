from django.urls import path
from mi.views import * 

urlpatterns = [
    path('caption/',caption,name='caption'),
    path('vice/',vice,name='vice'),
]
