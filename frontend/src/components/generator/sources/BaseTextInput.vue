<script setup lang="ts">
const model = defineModel();
model.value.type = 'text';
</script>

<template>
  <div>
    <label for="deck-generator__input" class="sr-only">Place your words, separated by commas</label>
    <textarea
      name="Words Input"
      id="deck-generator__input"
      class="bg-white dark:text-gray-900 w-full h-50 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2"
      placeholder="Place your words, separated by commas"
      v-model="model.content"
    ></textarea>
  </div>
</template>
