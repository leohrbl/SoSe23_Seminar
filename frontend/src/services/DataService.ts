import axios from 'axios';
import type Result from "@/types/Result";

const BASE_URL = 'http://127.0.0.1:8000';

async function getResultList(name: string, cardNumber: string, edition: string, rarity: string): Promise<Result[]> {
  const response = await axios.get(`${BASE_URL}/get/`, {
    params: {
      name,
      card_number: cardNumber,
      edition,
      rarity,
    },
  });

  return response.data.map((result: any) => ({
    name: result.name,
    edition: result.edition,
    rarity: result.rarity,
    number: result.card_number,
    price: result.market_price,
    shop: result.shop,
    productLink: result.product_link,
    picture: result.picture_url,
  }));
}

export {getResultList};