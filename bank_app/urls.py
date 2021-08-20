from django.contrib import admin
from django.urls import path
from .views import HomePageView, CreateCustomer, ViewAllCustomers, TransferMoney, TransferLogic

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('createCustomer/',CreateCustomer,name='createUser'),
    path('viewCustomers/',ViewAllCustomers.as_view(),name='viewAllCustomers'),
    path('transferMoney/',TransferMoney.as_view(),name='transfer'),
    path('transferLogic/',TransferLogic.as_view(),name='logic')
]