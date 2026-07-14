<script setup lang="ts">
import Card from '@/components/ui/Card.vue';
import { ref, computed } from 'vue';
import { ArrowLeftIcon, ArrowRightIcon } from '@heroicons/vue/16/solid';
import { useGeneratorStore } from '@/stores/generator';
import type { CardData } from '@/types/card';
import Modal from './Modal.vue';

const generatorStore = useGeneratorStore();
const currentIndex = ref(0);
const isAnimating = ref(false);
const showModal = ref(false);
function navigateCarousel(direction: 1 | -1) {
  if (generatorStore.cards.length <= 1 || isAnimating.value) return;
  isAnimating.value = true;
  setTimeout(() => {
    currentIndex.value =
      (currentIndex.value + direction + generatorStore.cards.length) % generatorStore.cards.length;
    isAnimating.value = false;
  }, 400);
}
const visibleCards = computed(() => {
  if (generatorStore.cards.length === 0) return [null, null, null];
  return [0, 1, 2].map(
    (i) => generatorStore.cards[(currentIndex.value + i) % generatorStore.cards.length] ?? null,
  );
});
const displayIndex = computed({
  get: () => currentIndex.value + 1,
  set: (val) => {
    const num = Number(val);
    currentIndex.value = Math.min(Math.max(num - 1, 0), generatorStore.cards.length - 1);
  },
});
function handleCardUpdate(updatedCard: CardData | null | undefined) {
  if (!updatedCard) return;
  generatorStore.updateCard(currentIndex.value, updatedCard);
}
</script>

<template>
  <div class="snap-center shrink-0 w-full max-w-[450px] mx-auto px-4">
    <div class="relative aspect-3/2">
      <Card
        v-for="(card, index) in visibleCards"
        @maximize="showModal = true"
        @click="navigateCarousel(1)"
        :key="card?.id ?? index"
        :card="card"
        @update:card="handleCardUpdate($event)"
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
        class="flex items-center justify-center bg-gray-100 rounded-lg px-4 h-10 text-sm font-medium"
      >
        <input
          type="number"
          min="1"
          :max="generatorStore.cards.length"
          class="w-12 border-none text-center focus:outline-none bg-transparent"
          v-model="displayIndex"
        />
        <span class="text-gray-400 mr-1">/</span>
        <p class="text-gray-600">{{ generatorStore.cards.length }}</p>
      </div>
      <ArrowRightIcon
        class="w-10 h-10 p-2 rounded-full bg-gray-100 cursor-pointer hover:bg-gray-200 transition-colors text-gray-600"
        @click="navigateCarousel(1)"
      />
    </div>
  </div>
  <Teleport to="body">
    <Transition name="modal">
      <div
        v-if="showModal"
        class="fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-20"
        @click.self="showModal = false"
      >
        <div class="w-full h-full">
          <Card
            :card="generatorStore.cards[currentIndex]"
            class="hover:translate-y-0! hover:translate-x-0!"
          />
        </div>
      </div>
    </Transition>
  </Teleport>
</template>
