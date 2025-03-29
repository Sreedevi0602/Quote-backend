from django.urls import path
from . import views
from myapp.views import *

urlpatterns = [
    path('', ReactView.as_view(), name="something"),
]