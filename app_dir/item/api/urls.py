from django.urls import path

from .views import (
    ItemUrlListAPIView, ItemUrlCreateAPIView, ItemUrlDetailAPIView, ItemUrlDeleteAPIView, UpdateAPIView,
    ItemPriceHistoryListAPIView, ItemPriceHistoryCreateAPIView, ItemPriceHistoryUpdate
)


urlpatterns = [
    path('', ItemUrlListAPIView.as_view(), name='item-url-list'),
    path('create/', ItemUrlCreateAPIView.as_view(), name='item-url-creator'),
    path('<int:pk>/', ItemUrlDetailAPIView.as_view(), name='item-url-detail'),
    path('delete/<int:pk>/', ItemUrlDeleteAPIView.as_view(), name='item-url-destroyer'),
    path('update/<int:pk>/', UpdateAPIView.as_view(), name='item-url-updater'),

    path('<int:pk>/history/', ItemPriceHistoryListAPIView.as_view(), name='item-price-history-list'),
    path('history/create/', ItemPriceHistoryCreateAPIView.as_view(), name='item-price-history-creator'),
    path('history/update/<int:id>/', ItemPriceHistoryUpdate.as_view(), name='item-price-history-updater'),
]
