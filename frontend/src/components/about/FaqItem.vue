<script setup lang="ts">
import { ref } from 'vue';
import { ChevronDownIcon } from '@heroicons/vue/16/solid';

const props = defineProps<{ question: string; answer: string }>();
const isOpen = ref(false);
</script>
<template>
  <div class="flex flex-col items-start border-b border-gray-200 py-4 gap-2 w-full">
    <button
      class="flex items-center justify-between text-left gap-4 cursor-pointer"
      @click="isOpen = !isOpen"
    >
      <span class="text-sm font-medium">{{ props.question }}</span>
      <ChevronDownIcon
        class="h-4 w-4 text-gray-400 shrink-0"
        :style="{
          transform: isOpen ? 'rotate(180deg)' : 'rotate(0deg)',
          transition: 'transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
        }"
      />
    </button>
    <Transition name="faq">
      <p v-if="isOpen" class="text-sm text-gray-500 leading-relaxed">
        {{ props.answer }}
      </p>
    </Transition>
  </div>
</template>
<style scoped>
.faq-enter-active,
.faq-leave-active {
  transition:
    opacity 0.2s ease,
    max-height 0.2s ease;
  overflow: hidden;
  max-height: 200px;
}

.faq-enter-from,
.faq-leave-to {
  opacity: 0;
  max-height: 0;
}
</style>
