<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="bg-gray-200 border-zinc-600 border-b-2">
      <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        <div class="flex items-center">
          <img src="/pokeball.svg" class="h-8 mr-3" alt="PokeCard24 Logo" />
          <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-zinc-600">PokeCard24</span>
        </div>
        <div class="hidden w-full md:block md:w-auto" id="navbar-default">
          <ul class="font-medium flex flex-col p-4 md:p-0 mt-4 rounded-lg md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white">
            <li class="text-center">
              <RouterLink to="/" class="block py-2 pl-3 pr-3 text-zinc-600 border-zinc-600 border-2 rounded-lg">Home</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <div class="bg-gray-200">
    <RouterView />
  </div>
</template>
