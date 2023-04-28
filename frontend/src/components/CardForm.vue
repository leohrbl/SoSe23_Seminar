<template>
    <div class="min-h-screen pb-60 flex flex-col justify-center">
      <div class="max-w-md w-full mx-auto">
        <div class="text-center font-medium text-3xl text-zinc-600">Preise zu einer Pokemonkarte vergleichen:</div>
      </div>
      <div class="max-w-md w-full mx-auto mt-4 bg-gray-200 p-8 border-solid border-zinc-600 rounded-md shadow-2xl shadow-black-500">
        <form @submit.prevent="$emit('submit', card)" class="max-w-md w-full mx-auto mt-4">
          <div>
            <label class="text-sm font-bold text-gray-600 block">Name</label>
            <input required v-model="card.name" type="text" class="w-full p-2 border border-gray-300 rounded-md mt-1"/>
          </div>
          <div class="pt-3">
            <label class="text-sm font-bold text-gray-600 block">Typ</label>
            <input required v-model="card.type" type="text" class="w-full p-2 border border-gray-300 rounded-md mt-1"/>
          </div>
          <div class="pt-3">
            <label class="text-sm font-bold text-gray-600 block">Nummer</label>
            <input required v-model="card.number" type="text" class="w-full p-2 border border-gray-300 rounded-md mt-1"/>
          </div>
          <div class="pt-3">
            <label class="text-sm font-bold text-gray-600 block">Zustand</label>
            <input required v-model="card.condition" type="text" class="w-full p-2 border border-gray-300 rounded-md mt-1"/>
          </div>
          <div class="pt-3">
            <label class="text-sm font-bold text-gray-600 block">Edition</label>
            <input required v-model="card.edition" type="text" class="w-full p-2 border border-gray-300 rounded-md mt-1"/>
          </div>
          <div class="pt-3">
            <label class="text-sm font-bold text-gray-600 block">Seltenheit</label>
            <input required v-model="card.rarity" type="text" class="w-full p-2 border border-gray-300 rounded-md mt-1"/>
          </div>
          <div class="flex items-center justify-center pt-5">
            <button type="submit" class="transition ease-in-out duration-75 hover:scale-105 border-solid border-2 border-zinc-600  bg-gradient-to-r from-50% from-white to-50% to-red-500 rounded-full font-bold py-2 px-4 text-zinc-600">
              Preise <span class="text-white">finden</span>
            </button>
          </div>
        </form>
      </div>
    </div>
</template>

<script lang="ts">
import type Card from "@/types/Card";
import { ref } from "vue";
export default {
  name: "CardForm",
  setup() {
    const card = ref({} as Card)

    return {
      card,
    }
  },
  emits: ["submit"]
}
</script>

<style>
input[type="text"]:focus {
    outline: 2px solid rgb(82 82 91);;
}
</style>
