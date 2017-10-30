from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Employees
from . serlizers import EmployeesSerializer

class Employee(APIView):
    def get(self,request):
        employees=Employees.objects.all()
        serializer=EmployeesSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
    