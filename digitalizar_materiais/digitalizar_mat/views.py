from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def soma(request):
    resultado = 6 + 6  
    return JsonResponse({'resultado': resultado})