from django.shortcuts import render


def viewsite(request):
	return render(request, 'index.html', {})