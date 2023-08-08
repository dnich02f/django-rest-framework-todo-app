from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Returns Task model object as JsonResponse object
    """
    class Meta:
        model = Task
        fields = '__all__'
