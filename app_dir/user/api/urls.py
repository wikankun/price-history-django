from django.urls import path

from .views import (
    UserListAPIView, UserCreateAPIView,
    UserDetailAPIView, UserDeleteAPIView,
    UpdateAPIView, UserProfileAPIView
)


urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-creator'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-profile'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile-self'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-destroyer'),
    path('update/<int:pk>/', UpdateAPIView.as_view(), name='user-updater')
]
