<script setup lang="ts">
import type { OptionItem } from '@/types/option';

const props = defineProps<{
  options: OptionItem[];
}>();
const selectedOption = defineModel<string>();
</script>

<template>
  <div class="inline-flex h-5 w-48 sm:w-auto md:w-full items-center justify-end bg-surface p-1">
    <button
      type="button"
      v-for="option in props.options"
      aria-disabled="false"
      class="group cursor-pointer inline-flex items-center justify-center whitespace-nowrap py-2 align-middle font-semibold transition-all duration-300 ease-in-out disabled:cursor-not-allowed stroke-blue-700 min-w-[32px] gap-1.5 text-sm disabled:stroke-slate-400 disabled:text-slate-400 hover:stroke-blue-950 hover:text-blue-950 h-7 text-slate-950 w-full first:rounded-bl-md first:rounded-tl-md last:rounded-br-md last:rounded-tr-md px-3 drop-shadow sm:w-auto"
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
