from rest_framework import serializers
from ..models import *


class ItemUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemUrl
        fields = [
            'id',
            'name',
            'url'
        ]
        
    def create(self, validated_data):
        name = validated_data['name']
        url = validated_data['url']
        item_url_obj = ItemUrl(
            name = name,
            url = url
        )
        item_url_obj.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.url = validated_data.get('url', instance.url)
        instance.save()

        return instance

class ItemPriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPriceHistory
        fields = [
            'price',
            'updated_at'
        ]

    def create(self, validated_data):
        item = validated_data['item']
        price = validated_data['price']
        item_price_obj = ItemPriceHistory(
            item = item,
            price = price
        )
        item_price_obj.save()
        return validated_data
