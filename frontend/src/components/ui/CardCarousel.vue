<script setup lang="ts">
import Card from '@/components/ui/Card.vue';
import { ref, computed } from 'vue';
import { ArrowLeftIcon, ArrowRightIcon, XMarkIcon } from '@heroicons/vue/16/solid';
import { useGeneratorStore } from '@/stores/generator';
import type { CardData } from '@/types/card';

const emit = defineEmits<{ 'all-cards-deleted': [] }>();
const generatorStore = useGeneratorStore();
const currentIndex = ref(0);
const isAnimating = ref(false);
const showModal = ref(false);
const totalCards = computed(() => generatorStore.cards.length);
const isDeckCleared = ref(false);
function navigateCarousel(direction: 1 | -1) {
  if (totalCards.value <= 1 || isAnimating.value) return;
  isAnimating.value = true;
  setTimeout(() => {
    currentIndex.value = (currentIndex.value + direction + totalCards.value) % totalCards.value;
    isAnimating.value = false;
  }, 400);
}
const visibleCards = computed(() => {
  if (totalCards.value === 0) return [null, null, null];
  return [0, 1, 2].map(
    (i) => generatorStore.cards[(currentIndex.value + i) % totalCards.value] ?? null,
  );
});
const displayIndex = computed({
  get: () => currentIndex.value + 1,
  set: (val) => {
    const num = Number(val);
    currentIndex.value = Math.min(Math.max(num - 1, 0), totalCards.value - 1);
  },
});
function handleCardUpdate(updatedCard: CardData | null | undefined) {
  if (!updatedCard) return;
  generatorStore.updateCard(currentIndex.value, updatedCard);
}
function handleCardDelete() {
  const indexToDelete = currentIndex.value;
  generatorStore.deleteCard(indexToDelete);
  if (totalCards.value === 0) {
    isDeckCleared.value = true;
  }
}
</script>

<template>
  <div class="snap-center shrink-0 w-full max-w-[450px] mx-auto px-4" v-if="!isDeckCleared">
    <div class="relative aspect-3/2">
      <Card
        v-for="(card, index) in visibleCards"
        @maximize="showModal = true"
        @delete="handleCardDelete()"
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
  <div class="flex flex-col items-center justify-center" v-else>
    <h3 class="text-xl font-bold text-neutral">
      Your deck is <span class="text-accent">empty</span>
    </h3>
    <p class="mb-5 text-xs text-gray-500 max-w-sm leading-relaxed">
      All cards have been removed from this batch.
    </p>
    <button
      @click="generatorStore.currentStep = 0"
      class="group cursor-pointer select-none rounded-xl bg-primary px-8 py-4 font-semibold text-surface shadow-md transition-all duration-200 hover:-translate-y-0.5 hover:bg-opacity-95 hover:text-primary-muted hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-primary/50"
    >
      <span class="flex items-center justify-center gap-2">
        Ready to build something new?
        <span class="transition-transform duration-200 group-hover:translate-x-1">→</span>
      </span>
    </button>
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
