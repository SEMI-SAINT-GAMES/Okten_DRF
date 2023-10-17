from django.urls import include, path

from apps.user.views import UserListCreateAPIView, UserAddAutoparkView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='get_all_users'),
    path('/<int:pk>/autopark', UserAddAutoparkView.as_view(), name='add_autopark_user'),
    path('/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='get-user_by_id')
]