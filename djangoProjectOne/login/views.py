from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("<h2>This is my login page!!</h2>")