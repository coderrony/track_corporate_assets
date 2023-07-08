from rest_framework import serializers
from .models import Company, Employee, Device, History


class CompanySerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class HistorySerializer(serializers.ModelSerializer):
    device = serializers.StringRelatedField()

    class Meta:
        model = History
        fields = "__all__"
