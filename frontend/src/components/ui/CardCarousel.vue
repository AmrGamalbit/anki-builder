<script setup lang="ts">
import Card from '@/components/ui/Card.vue';
import { ref, computed } from 'vue';
import { ArrowLeftIcon, ArrowRightIcon } from '@heroicons/vue/16/solid';

const props = defineProps(['cards']);
const currentIndex = ref(0);
const isAnimating = ref(false);
function navigateCarousel(direction: 1 | -1) {
  if (props.cards.length <= 1 || isAnimating.value) return;
  isAnimating.value = true;
  setTimeout(() => {
    currentIndex.value = (currentIndex.value + direction) % props.cards.length;
    isAnimating.value = false;
  }, 400);
}
const visibleCards = computed(() => {
  if (props.cards.length === 0) return [null, null, null];
  return [0, 1, 2].map((i) => props.cards[(currentIndex.value + i) % props.cards.length]);
});
const displayIndex = computed({
  get: () => currentIndex.value + 1,
  set: (val) => {
    const num = Number(val);
    currentIndex.value = Math.min(Math.max(num - 1, 0), props.cards.length - 1);
  },
});
</script>

<template>
  <div class="snap-center shrink-0 w-full max-w-[450px] mx-auto px-4">
    <div class="relative aspect-3/2">
      <Card
        v-for="(card, index) in visibleCards"
        @click="navigateCarousel(1)"
        :key="card?.id ?? index"
        :card="card"
        class="absolute top-0 w-full transition-all duration-300 ease-in-out cursor-pointer"
        :style="{
          zIndex: 3 - index,
          transform:
            isAnimating && index === 0
              ? 'translate(120%, -20px) rotate(15deg)'
              : `translate(${20 * index}px, ${10 * index}px) scale(${1 - index * 0.05})`,
          opacity: isAnimating && index === 0 ? 0 : 1,
        }"
      />
    </div>
    <div class="flex justify-center items-center m-10 select-none gap-2">
      <ArrowLeftIcon
        class="w-10 h-10 p-2 rounded-full bg-gray-100 cursor-pointer hover:bg-gray-200 transition-colors text-gray-600"
        @click="navigateCarousel(-1)"
      />
      <div
        class="flex items-center justify-center bg-gray-100 rounded-lg px-4 h-10 gap-1 text-sm font-medium"
      >
        <input
          type="number"
          min="1"
          :max="props.cards.length"
          class="w-7 border-none text-right focus:outline-none bg-transparent"
          v-model="displayIndex"
        />
        <span class="text-gray-400">/</span>
        <p class="text-gray-600">{{ props.cards.length }}</p>
      </div>
      <ArrowRightIcon
        class="w-10 h-10 p-2 rounded-full bg-gray-100 cursor-pointer hover:bg-gray-200 transition-colors text-gray-600"
        @click="navigateCarousel(1)"
      />
    </div>
  </div>
</template>
