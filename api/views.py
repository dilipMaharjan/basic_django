from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView)
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Employees
from api.pagination import PageNumberPagination
from api.permissions import IsOwnerOrReadOnly
from api.serlizers import (EmployeesListSerializer,
                           EmployeesDetailSerializer)


#different view type for different REST calls
class Employee(APIView):
    def get(self,request):
        employees=Employees.objects.all()
        serializer=EmployeesListSerializer(employees,many=True)
        return Response(serializer.data)

class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesListSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmplyeeWithListAPIView(ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesDetailSerializer
   # pagination_class = LimitOffsetPagination
    pagination_class = PageNumberPagination

class EmplyeeDetailAPIView(RetrieveAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesListSerializer
    lookup_field = 'pk' #pk can be changed to any of the field name

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(self.request.user)

class EmployeeDeleteAPIView(DestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesDetailSerializer