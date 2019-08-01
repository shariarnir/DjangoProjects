from django.http import HttpResponse

def home(request):
	return HttpResponse("<h1 style='color:red;'>This is first django project home page.!!</h1>")
