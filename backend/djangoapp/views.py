from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .serializers import CardSerializer
from .serializers import ResultSerializer
from scraper import scraper


@api_view(['GET'])
def card_list_prices(request, format=None):
    if request.method == 'GET':
        card_serializer = CardSerializer(data=request.query_params)
        if card_serializer.is_valid():
            card = card_serializer.create(validated_data=request.query_params)
            results = scraper.run_scraper(card)
            result_serializer = ResultSerializer(results, many=True)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST("Please fill in valid data for the price search"))
        return JsonResponse(result_serializer.data, status=status.HTTP_200_OK, safe=False)
