
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="home"),

    path('company/', views.CompanyAll.as_view(), name="company"),
    path('company/<int:pk>', views.CompanyDetails.as_view(), name="companyDetails"),

    path('employee/', views.EmployeeAll.as_view(), name="employee"),
    path('employee/<int:pk>', views.EmployeeDetails.as_view(), name="companyDetails"),

    path('device/', views.DeviceAll.as_view(), name="device"),
    path('device/<int:pk>', views.DeviceDetails.as_view(), name="deviceDetails"),

    path('history/', views.HistoryAll.as_view(), name="history"),



]
