from django.shortcuts import render,HttpResponse

def home(request):
	#return HttpResponse("<h1 style='color:orange;'>AccountPage</h1>");
	return render(request,'accounts/login.html')
