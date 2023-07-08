from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employee")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Device(models.Model):

    CONDITION_CHOICES = [
        ("CHECKOUT", 'Checked Out'),
        ("RETURN", 'Returned'),
    ]
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    condition = models.CharField(
        choices=CONDITION_CHOICES,  max_length=30)

    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class History(models.Model):
    device = models.ForeignKey(
        Device, on_delete=models.Case, related_name="device")
    condition_status = models.CharField(max_length=10)
    last_update = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.device.name
