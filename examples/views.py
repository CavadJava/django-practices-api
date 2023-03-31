from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from examples.form import EmpForm, StudentForm
from examples.models import FoodDb
from examples.serializer import FoodSerializer


def index(request):
    return render(request, 'index.html')


def indexForm(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/api/index')
            except:
                pass
    else:
        form = EmpForm()

    return render(request, "index_form.html", {'form': form})


def indexStudent(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request, "index_form.html", {'form': student})


def handle_uploaded_file(f):
    with open('examples/static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# Create your views here.
@api_view(['GET'])
def getFood(request):
    food = FoodDb.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getHello(request):
    return Response()


@api_view(['POST'])
def postFood(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
