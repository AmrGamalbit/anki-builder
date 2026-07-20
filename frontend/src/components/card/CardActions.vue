<script setup lang="ts">
import { ArrowsRightLeftIcon, TrashIcon } from '@heroicons/vue/16/solid';

const currentSide = defineModel();
const emit = defineEmits<{ delete: [] }>();
const flipCard = () => {
  currentSide.value == 'front' ? (currentSide.value = 'back') : (currentSide.value = 'front');
};
</script>

<template>
  <div class="flex items-center mt-1 md:mt-2 shrink-0">
    <button
      class="flex-1 w-8 h-8 flex justify-center items-center cursor-pointer text-gray-400 hover:text-gray-600 hover:bg-gray-200 rounded-bl-lg transition-all duration-200 ease-in-out"
      @click.stop="flipCard"
    >
      <ArrowsRightLeftIcon class="h-5 w-5" />
    </button>
    <button
      class="flex items-center justify-center cursor-pointer rounded-br-lg p-2 text-gray-400 transition-colors hover:bg-red-50 hover:text-red-600"
      @click.stop="$emit('delete')"
    >
      <TrashIcon class="h-5 w-5" />
    </button>
  </div>
</template>
