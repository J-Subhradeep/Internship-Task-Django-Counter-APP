from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CountDB
from .serializers import CountDBSerializer

# Create your views here.


class AddLike(APIView):
    def post(self, request, *args, **kwargs):
        if not CountDB.objects.all():
            obj = CountDB(likes=1, dislikes=0)
            obj.save()
            return Response({'likes': 1, 'dislikes': 0})
        else:
            obj = list(CountDB.objects.all())
            obj = obj[-1]
            obj.likes += 1
            obj.save()
            return Response({'likes': obj.likes, 'dislikes': obj.dislikes})


class GetLikesAndDislikes(APIView):
    def get(self, request, *args, **kwargs):
        obj = list(CountDB.objects.all())

        if obj:
            obj = obj[-1]
            return Response({'likes': obj.likes, 'dislikes': obj.dislikes})
        else:
            return Response({'likes': 0, 'dislikes': 0})


class AddDislike(APIView):
    def post(self, request, *args, **kwargs):
        if not CountDB.objects.all():
            obj = CountDB(likes=1, dislikes=0)
            obj.save()
            return Response({'likes': 0, 'dislikes': 1})
        else:
            obj = list(CountDB.objects.all())
            obj = obj[-1]
            obj.dislikes += 1
            obj.save()
            return Response({'likes': obj.likes, 'dislikes': obj.dislikes})
