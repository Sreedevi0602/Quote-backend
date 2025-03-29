from django.shortcuts import render, redirect
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from .forms import QuoteForm
from django.http import JsonResponse

# Create your views here.



# Admin HTML form for submitting quotes
def submit_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("submit_quote")  # Reload form after submission
    else:
        form = QuoteForm()

    return render(request, "submit_quote.html", {"form": form})

# API to fetch quotes for React frontend
class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        detail = [{"name": detail.name, "detail": detail.detail} for detail in React.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# API to return JSON quotes for React
def get_quotes(request):
    quotes = React.objects.all().values('name', 'detail')
    return JsonResponse(list(quotes), safe=False)
