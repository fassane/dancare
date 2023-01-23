# importing required packages

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from diab_retina_app import process


@csrf_exempt
def display(request):
    if request.method == 'GET':
        return render(request, 'app.html')

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

@csrf_exempt
def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')

@csrf_exempt
def fonction(request):
    if request.method == 'GET':
        return render(request, 'fonction.html')

@csrf_exempt
def demo(request):
    if request.method == 'GET':
        return render(request, 'demo.html')

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        img = request.POST.get('image')
        response = process.process_img(img)
        return HttpResponse(response, status=200)
