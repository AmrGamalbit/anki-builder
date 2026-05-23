<script setup lang="ts">
const pickedColor = defineModel<string>();
</script>

<template>
  <input
    type="color"
    class="p-1 h-10 w-14 block bg-layer border border-layer-line cursor-pointer rounded-lg disabled:opacity-50 disabled:pointer-events-none"
    id="hs-color-input"
    title="Choose your color"
    v-model="pickedColor"
  />
</template>
0
