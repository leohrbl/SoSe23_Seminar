from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from rest_framework import status
from .models import Card
from .serializers import CardSerializer
from .serializers import ResultSerializer


class GetScraperResults(APIView):
    cardSerializer = CardSerializer
    resultSerializer = ResultSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)
