from django.contrib.auth.models import User
from rest_framework import serializers
from admin_api.models.models import Task


class TaskSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Task
        fields = ['id', 'create_date', 'title', 'description', 'state', 'creator']


class UserSerializer(serializers.ModelSerializer):
    created_tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'created_tasks', 'password']
        write_only_fields = ['password']
        read_only_fields = ['id']
