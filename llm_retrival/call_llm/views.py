from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.
def home(request):
    return HttpResponse ("hello")



class ReturnTwoAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response(2, status=status.HTTP_200_OK)
