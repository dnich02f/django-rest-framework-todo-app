from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import TaskSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-crete/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    print("Request.data: ", request.data)
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item successfully delete!')
