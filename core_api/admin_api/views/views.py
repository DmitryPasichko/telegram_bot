from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from admin_api.models.models import Task
from admin_api.serializers.serializer import TaskSerializer, UserSerializer
from rest_framework import generics, permissions, mixins
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from util import deprecated
# from rest_framework.parsers import JSONParser
# from django.http import Http404
# from rest_framework.views import APIView
# from django.http import JsonResponse, HttpRequest

@csrf_exempt
@deprecated("Deprecated. Use TaskList class")
def task_list(request):
    """
    List all task, or create a new task.
    """
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass


@csrf_exempt
@deprecated("Deprecated. Use TaskDetail class")
def task_details(request, id):
    """
    Retrieve, update or delete task.
    """
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


class TaskList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    List all task, or create a new task.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        from django.contrib.auth.hashers import make_password
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     tasks = Task.objects.all()
    #     serializer = TaskSerializer(tasks, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    #
    # def post(self, request, format=None):
    #     data = JSONParser().parse(request)
    #     serializer = TaskSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a task instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def get_object(self, pk):
    #     try:
    #         return Task.objects.get(pk=pk)
    #     except Task.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, id, format=None):
    #     task = self.get_object(id)
    #     serializer = TaskSerializer(task)
    #     return JsonResponse(serializer.data)
    #
    # def put(self, request, id, format=None):
    #     task = self.get_object(id)
    #     data = JSONParser().parse(request)
    #     serializer = TaskSerializer(task, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)
    #
    # def delete(self, request, id, format=None):
    #     task = self.get_object(id)
    #     task.delete()
    #     return HttpResponse(status=204)


class UserList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if 'password' in request.data:
            request.data['password'] = make_password(request.data['password'])
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
