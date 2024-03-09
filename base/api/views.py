from django.shortcuts import render
from django.http import JsonResponse
import requests

def Get(request):
    res = requests.get("http://localhost:10000/api/user").json()
    return JsonResponse(res,safe=False)
