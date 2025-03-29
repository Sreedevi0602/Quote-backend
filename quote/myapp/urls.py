from django.urls import path
from . import views
from myapp.views import *

urlpatterns = [
    path("submit-quote/", submit_quote, name="submit_quote"),  # Admin form
    path("wel/", ReactView.as_view(), name="something"),  # API for React
    path("api/quotes/", get_quotes, name="get_quotes"),  # API for React
]