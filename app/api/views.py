from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class Test(APIView):
    def post(self, request, id, format=None):                            
        return Response(status=status.HTTP_200_OK)       