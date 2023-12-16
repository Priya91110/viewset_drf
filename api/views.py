from django.shortcuts import render
from .models import Car, CarSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
# creating view set


class CarViewSet(ViewSet):
    # action method internally called(get,put,post)
    # primary key based
    def list(self, request):
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
            
    # non primary key based
    def retrieve(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    
    def destroy(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response({"message": f"Car with ID {pk} is deleted successfully"})
        except Car.DoesNotExist:
            return Response({"error": f"Car with ID {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk):
        serializer = CarSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)