from rest_framework import serializers
from .models import Task

#serializers gives us the option to return any model data as a Json response

#create classes of models that you want to serialize
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        