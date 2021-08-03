from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task



# Create your views here.

@api_view(['GET'])
def crudFunc(request):
    #if anyone wants to see the url patterns while working with the api endpoints
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		} 

    return Response(api_urls)

#gives reponse of all the data
@api_view(['GET'])
def taskList(request):
    #query out database
    tasks = Task.objects.all()
    #serialize the data
    serializer = TaskSerializer(tasks, many=True)
    #return the response
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False) #many=Flase returns just one object based on the pk
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    #like models forms if serializer is valid it will save the data
    if serializer.is_valid():
        serializer.save()

    #and return the response
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    #like a form we have to set an instance
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    #get a task, no need to serialize it and delete it
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('item successfully deleted')