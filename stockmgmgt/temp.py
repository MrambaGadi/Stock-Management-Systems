from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
	title = 'Welcome: This is the Home Page'
	form = 'Welcome: This is the Home Page'
	context = {
		"title": title,
		"test": form,
	}
	return render(request, "home.html",context)


def list_item(request):
	title = 'List of Items'
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_item.html", context)


def add_item(request):
	form = AddItemForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_item.html", context)