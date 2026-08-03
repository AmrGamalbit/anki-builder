<script setup lang="ts">
import type { OptionItem } from '@/types/option';

const props = defineProps<{
  options: OptionItem[];
}>();
const selectedOption = defineModel<string>();
</script>

<template>
  <div
    class="inline-flex flex-col md:flex-row w-48 sm:w-auto md:w-full items-center justify-end bg-surface p-1"
  >
    <button
      type="button"
      v-for="option in props.options"
      aria-disabled="false"
      class="leading-tight w-full md:w-fit cursor-pointer inline-flex items-center justify-center whitespace-nowrap px-3 py-1 text-sm font-semibold text-slate-950 transition-colors duration-200 disabled:cursor-not-allowed disabled:text-slate-400 first:rounded-t-md last:rounded-b-md md:first:rounded-l-md md:first:rounded-tr-none md:last:rounded-r-md md:last:rounded-bl-none drop-shadow"
      :class="
        selectedOption === option.value
          ? 'bg-primary dark:text-white hover:bg-primary/80'
          : 'bg-white hover:bg-gray-50'
      "
      @click="selectedOption = option.value"
    >
      {{ option.label }}
    </button>
  </div>
</template>
