from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from .models import Card

class GetScraperResults(APIView):
    def get(self, request, format=None):
        name = self.request.query_params.get('name', None)
        card_type = self.request.query_params.get('card_type', None)
        card_number = self.request.query_params.get('card_number', None)
        condition = self.request.query_params.get('condition', None)
        edition = self.request.query_params.get('edition', None)
        rarity = self.request.query_params.get('rarity', None)

        card = Card(name=name, card_type=card_type, card_number=card_number, condition=condition, edition=edition, rarity=rarity)
        
        return None
