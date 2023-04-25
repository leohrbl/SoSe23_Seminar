from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Result
from .models import Card
from .serializers import CardSerializer
from .serializers import ResultSerializer


@api_view(['GET'])
def card_list_prices(request, format=None):
    if request.method == 'GET':
        card_serializer = CardSerializer(data=request.query_params)
        card = None
        if card_serializer.is_valid():
            card = card_serializer.create(validated_data=request.query_params)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST("Please fill in valid data for the price search"))
        return Response(card_serializer.data, status=status.HTTP_200_OK)
