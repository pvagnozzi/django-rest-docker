from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Peripheral(APIView):
    def post(self, request, id, format=None):            
        peripheral_id = id
        print("Execute " + str(peripheral_id))
        return Response(status=status.HTTP_200_OK)       