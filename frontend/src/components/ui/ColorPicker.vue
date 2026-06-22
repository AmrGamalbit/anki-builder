<script setup lang="ts">
const pickedColor = defineModel<string>();
</script>

<template>
  <input
    type="color"
    class="w-10 h-4 rounded cursor-pointer ring-1 ring-gray-500 ring-offset-0 bg-transparent [&::-webkit-color-swatch-wrapper]:p-0 [&::-webkit-color-swatch]:rounded [&::-webkit-color-swatch]:border-0"
    id="hs-color-input"
    title="Choose your color"
    v-model="pickedColor"
  />
</template>
