from rest_framework import viewsets
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, pagination
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from .models import *

class CaregiverViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = CaregiverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = Caregiver.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = CaregiverSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Caregiver.objects.all()
        caregiver = get_object_or_404(queryset, pk=pk)
        serializer = CaregiverSerializer(caregiver)
        return Response(serializer.data)

    def update(self, request, pk=None):
        caregiver = Caregiver.objects.get(pk=pk)
        serializer = CaregiverSerializer(caregiver, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        caregiver = Caregiver.objects.get(pk=pk)
        caregiver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = Customers.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = CustomerSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customers.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        customer = Customers.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        customer = Customers.objects.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShiftViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = ShiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = Shifts.objects.all()
        serializer = ShiftSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Shifts.objects.all()
        shift = get_object_or_404(queryset, pk=pk)
        serializer = ShiftSerializer(shift)
        return Response(serializer.data)

    def update(self, request, pk=None):
        shift = Shifts.objects.get(pk=pk)
        serializer = ShiftSerializer(shift, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        shift = Shifts.objects.get(pk=pk)
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)