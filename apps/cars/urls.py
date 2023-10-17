from django.urls import include, path

from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroyView, CarsInAutopark

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
    path('/autopark/<int:pk>', CarsInAutopark.as_view())
]