from django.http import HttpResponse

def home(request):
	return HttpResponse("<h1 style='color:red;'>Home Page!!</h1>")
