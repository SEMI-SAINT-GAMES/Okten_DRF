from django.urls import include, path
from apps.users_requests.views import ListCreatePartRequestView

urlpatterns = [
    path('', ListCreatePartRequestView.as_view(), name='ListCreatePartRequestView')
]