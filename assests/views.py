from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework import generics

from .models import Company, Employee, Device, History
from .serializer import CompanySerializer, EmployeeSerializer, DeviceSerializer, HistorySerializer


from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.


def home(request):
    return redirect("company")


class CompanyAll(generics.ListCreateAPIView):  # Accept Request get,post
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# Accept Request get, put, patch and delete
class CompanyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeAll(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceAll(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


# history create automatic when created Device
@receiver(post_save, sender=Device)
def create_history_entry(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            device=instance, condition_status=instance.condition, last_update=instance.timestamp)


class HistoryAll(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
