from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Views como Controller
# Recebe resquest e devolve response

# @app.get('rogerio') no FastAPI
def hello(request):
  return HttpResponse('Hello Rogério S2')