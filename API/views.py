from rest_framework.views import APIView 
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from main.models import *
from .serializer import *

# Create your views here.

class AppSerializer(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    def get(self,request):
        data =list(Apps.objects.values())
        return JsonResponse(data ,safe = False)

class View_appSerializer(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    def get(self,request,id):
        queryset = Apps.objects.get(id=id)
        return Response(str({'id':queryset.id,
        'name':queryset.app_name,
        'category':queryset.category,
        'point':queryset.point
        }))

class AddAppSerializer(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [BasicAuthentication]
    def get(self,request):
        data =list(Apps.objects.values())
        return JsonResponse(data ,safe = False)