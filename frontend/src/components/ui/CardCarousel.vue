<script setup lang="ts">
import Card from '@/components/ui/Card.vue';
import { ref, computed } from 'vue';

const props = defineProps(['cards']);
const currentIndex = ref(0);
const isAnimating = ref(false);
function showNextCard() {
  if (props.cards.length <= 1 || isAnimating.value) return;
  isAnimating.value = true;
  setTimeout(() => {
    currentIndex.value = (currentIndex.value + 1) % props.cards.length;
    isAnimating.value = false;
  }, 400);
}
const visibleCards = computed(() => {
  if (props.cards.length === 0) return [null, null, null];
  return [0, 1, 2].map((i) => props.cards[(currentIndex.value + i) % props.cards.length]);
});
</script>

<template>
  <div class="snap-center shrink-0 w-full max-w-[450px] mx-auto px-4">
    <div class="relative">
      <Card
        v-for="(card, index) in visibleCards"
        @click="showNextCard"
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
  </div>
</template>
