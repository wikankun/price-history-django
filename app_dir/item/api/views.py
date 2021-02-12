from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from json import dumps
from django.db.models import Q
from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemUrlSerializer, ItemPriceHistorySerializer
from ..models import *
from ..scrapper.scrapper import ScrapperTokopedia
from ...core.pagination import PostLimitOffsetPagination


class ItemUrlListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemUrlSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        queryset_list = ItemUrl.objects.all()
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(url__icontains=query)
            )

        return queryset_list.order_by('id')


class ItemUrlCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemUrlSerializer
    queryset = ItemUrl.objects.all()


class ItemUrlDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemUrlSerializer
    def get_queryset(self):
        return ItemUrl.objects.all()


class ItemUrlDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemUrlSerializer
    def get_queryset(self):
        return ItemUrl.objects.all()


class UpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemUrlSerializer
    def get_queryset(self):
        return ItemUrl.objects.all()

    def perform_update(self, serializer):
        serializer.save(itemurl=self.request.itemurl)

class ItemPriceHistoryListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemPriceHistorySerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = ItemPriceHistory.objects.filter(
            item = self.kwargs['pk']
        )

        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10

        return queryset_list.order_by('-id')

class ItemPriceHistoryCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemPriceHistorySerializer
    queryset = ItemPriceHistory.objects.all()

class ItemPriceHistoryUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        item = ItemUrl.objects.filter(id = id)[0]

        s = ScrapperTokopedia(item.url)
        price = s.getPrice()
        print(s.getProductName())
        print(s.getPrice())
        item_price_obj = ItemPriceHistory(
            item = item,
            price = price
        )
        item_price_obj.save()
        result = {
            'item': item_price_obj.item.id,
            'price': item_price_obj.price,
            'updated_at': item_price_obj.updated_at
        }
        
        return Response(result)
