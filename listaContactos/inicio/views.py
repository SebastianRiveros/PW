from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myHomeView(*args, **kwargs):
	return HttpResponse('<h1>Hola mundo desde Django</h1>')

def anotherView(request):
	return HttpResponse('<h1>Solo otra pagina</h1>')