from django.urls import include, path

from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('cars/<int:pk>', CarRetrieveUpdateDestroyView.as_view())
]