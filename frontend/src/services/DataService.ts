import http from "../http-common";
import type Card from "@/types/Card"

class DataService {

  getCardParams(card: Card) {
    const params = new URLSearchParams();
    params.append('name', card.name);
    params.append('type', card.type);
    params.append('number', card.number);
    params.append('condition', card.condition);
    params.append('edition', card.edition);
    params.append('rarity', card.rarity);
    return params;
  }

  getCardPrices(card: Card) {
    return http.get('/get', {
      params: this.getCardParams(card)
    })
  }
}

export default new DataService()