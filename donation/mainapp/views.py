from django.shortcuts import render

# Create your views here.
def home(request):
	dicty = [{
		'Name': 'kwame', 
		'Age':25,
	}], 
	context={
		'dicty': dicty,		
	}
	return render(request, 'pages/home.html', context)
