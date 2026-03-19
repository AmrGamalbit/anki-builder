<script setup lang="ts">
import { useId } from 'vue';

const id = useId();
const isEnabled = defineModel<boolean>({ default: false });
</script>

<template>
  <div class="relative inline-block w-11 h-5">
    <input
      :id="id"
      type="checkbox"
      class="peer appearance-none w-11 h-5 bg-accent dark:bg-gray-300 rounded-full checked:bg-primary cursor-pointer transition-colors duration-300"
      v-model="isEnabled"
    />
    <label
      :for="id"
      class="absolute top-0 left-0 w-5 h-5 bg-white rounded-full border border-slate-300 shadow-sm transition-transform duration-300 peer-checked:translate-x-6 peer-checked:border-slate-800 cursor-pointer"
    >
    </label>
  </div>
</template>
