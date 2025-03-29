from django.urls import path
from . import views
from myapp.views import *

urlpatterns = [
    path('wel/', ReactView.as_view(), name="something"),
]