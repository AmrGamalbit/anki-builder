<script setup lang="ts">
const currentStep = defineModel({ default: 0 });
</script>

<template>
  <div class="w-full">
    <div class="relative flex items-center justify-between w-full">
      <div class="absolute left-0 top-2/4 h-0.5 w-full -translate-y-2/4 bg-gray-300"></div>
      <div
        class="absolute left-0 top-2/4 h-0.5 w-full -translate-y-2/4 bg-gray-900 transition-all duration-500"
      ></div>
      <div
        v-for="step in 5"
        class="relative z-10 grid w-10 h-10 font-bold text-gray-900 transition-all duration-300 bg-gray-300 rounded-full place-items-center"
        :class="currentStep + 1 == step ? 'bg-gray-900 text-white' : ''"
      >
        {{ step }}
      </div>
    </div>
  </div>
</template>
