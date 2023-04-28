<template>
 <div>{{$props.card.name}}</div>
</template>

<script lang="ts">
import type Card from "@/types/Card";
export default {
  name: "PriceResultDetail",
  setup() {

  },
  props: {
    card : {} as Card
  }

};
</script>

<style scoped>

</style>