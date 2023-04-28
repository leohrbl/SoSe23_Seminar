<script lang="ts">
import CardForm from "@/components/CardForm.vue"
import type Card from "@/types/Card";
import PriceResultDetail from "@/components/PriceResultDetail.vue";
import { ref } from "vue";
export default {
  name: "HomeView",
  components: {
    PriceResultDetail,
    CardForm
  },
  setup() {
    const submit = (card: Card) => {
      console.log(card.name)
      cardProp.value = card
      console.log(cardProp.value.name)
      submitted.value = true
    }
    let cardProp = ref({} as Card)
    const submitted = ref<boolean>(false)

    return {
      submit,
      submitted,
      cardProp
    }
  }
}
</script>

<template>
  <CardForm v-if="!submitted" @submit="submit"></CardForm>
  <PriceResultDetail v-if="submitted" :card="cardProp"></PriceResultDetail>
</template>
