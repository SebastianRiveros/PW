from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myHomeView(request, *args, **kwargs):
	myContext = {
		'myText' : 'Esto es sobre nosotros',
		'myNumber' : '123',
	}
	print(args, kwargs)
	print(request.user)
	return render(request,"home.html",myContext)

def anotherView(request):
	return HttpResponse('<h1>Solo otra pagina</h1>')