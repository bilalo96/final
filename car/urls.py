from django.urls import path
from .views import CarList,CarDetail
from .api_view import CarAPIList, CarAPIDetail

app_name='car'


urlpatterns = [
    path('',CarList.as_view(),name='car_list'),
    path('<slug:slug>',CarDetail.as_view(),name='car_detail'),

    path('api/list',CarAPIList.as_view(),name='car_api_list'),
    path('api/list/<int:pk>',CarAPIDetail.as_view(),name='car_api_detail'),

]
