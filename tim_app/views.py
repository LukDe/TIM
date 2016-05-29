from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'tim_app/login.html')

def list(request):
	return render(request, 'tim_app/list.html')
