from rest_framework import serializers
from api.models import Employees

#writing different serializers for different view
class EmployeesListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('first_name','last_name')

class EmployeesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        # fields=('first_name','last_name')
        fields='__all__'