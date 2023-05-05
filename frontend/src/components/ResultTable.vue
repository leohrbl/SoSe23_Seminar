<template>
  <section class="container mx-auto p-6 min-h-screen">
    <div class="w-full mb-8 overflow-hidden rounded-lg shadow-lg">
      <div class="w-full overflow-x-auto">
        <table class="w-full">
          <thead>
          <tr class="text-md font-semibold tracking-wide text-left text-gray-900 bg-gray-100 uppercase border-b border-gray-600">
            <th class="px-4 py-3">Name</th>
            <th class="px-4 py-3">Edition</th>
            <th class="px-4 py-3">Seltenheit</th>
            <th class="px-4 py-3">Nummer</th>
            <th class="px-4 py-3">Marktpreis</th>
            <th class="px-4 py-3">Anbieter</th>
            <th class="px-4 py-3">Produkt Link</th>
          </tr>
          </thead>
          <tbody class="bg-white">
          <tr v-for="(result, index) in displayedData" :key="index" class="text-gray-700 hover:bg-red-300">
            <td class="px-4 py-3 border">
              <div class="flex items-center text-sm justify-between">
                <!-- <img class="mr-12 flex w-50" :src="result.picture" alt="card picture">
                <span class="text-lg ml-12">{{result.name}}</span>
                -->
                {{result.name}}
              </div>
            </td>
            <td class="px-4 py-3 border">
              <div class="flex items-center text-sm">
                {{result.edition}}
              </div>
            </td>
            <td class="px-4 py-3 border">
              <div class="flex items-center text-sm">
                {{result.rarity}}
              </div>
            </td>
            <td class="px-4 py-3 border">
              <div class="flex items-center text-sm">
                {{result.number}}
              </div>
            </td>
            <td class="px-4 py-3 border">
              <div class="flex items-center text-sm">
                {{result.price}}
              </div>
            </td>
            <td class="px-4 py-3 border">
              <div class="flex items-center text-sm">
                {{result.shop}}
              </div>
            </td>
            <td class="px-4 py-3 border">
              <div class="flex items-center text-sm">
                <a class="underline" :href="result.productLink" target="_blank">Click Here</a>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
<script lang="ts">
import type Result from "@/types/Result";
import { ref } from "vue";
export default {
  name: "ResultTable",
  setup(props : {results : Result[]}) {
    const displayedData = ref<Result[]>(props.results)

    return {
      displayedData
    }
  },
  props: {
    results : {} as Result[]
  }
};
</script>

<style scoped>

</style>