<script setup lang="ts">
const deckName = defineModel();
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Review</h2>
    <hr class="m-5" />
    <div class="flex flex-col gap-5">
      <div class="flex justify-between items-center">
        <h2 class="text-gray-900 dark:text-gray-100">Deck Name</h2>
        <div class="w-48 max-w-sm min-w-[200px]">
          <input
            class="inline-flex h-9 w-48 bg-white placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
            placeholder="Type here..."
            v-model="deckName"
          />
        </div>
      </div>
    </div>
  </section>
</template>
