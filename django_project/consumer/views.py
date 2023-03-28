from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def todos(request):
    response = requests.get('http://127.0.0.1:8000/api/')
    todos = response.json()
    print(todos)

    return render(request,"todo.html",{'todos':todos})
  