from rest_framework import serializers
from .models import Card
from .models import Result


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def create(self, validated_data):
        card = Card(**validated_data)
        return card


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

    def create(self, validated_data):
        result = Card(**validated_data)
        return result
