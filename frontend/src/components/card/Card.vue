<script setup lang="ts">
import { useGeneratorStore } from '@/stores/generator';
import { ref, computed } from 'vue';
import type { CSSProperties } from 'vue';
import { WindowIcon } from '@heroicons/vue/16/solid';
import type { CardData } from '@/types/card';
import CardSkeleton from './CardSkeleton.vue';
import CardBack from './CardBack.vue';
import CardFront from './CardFront.vue';
import CardActions from './CardActions.vue';

const emit = defineEmits<{ maximize: []; delete: [] }>();
const card = defineModel<CardData | null>('card');
const generatorStore = useGeneratorStore();
const appearanceOptions = generatorStore.appearanceOptions;
const currentSide = ref('front');

function handleUpdateCard(value: string, field: 'term' | 'definition') {
  if (!card.value) return;
  card.value = { ...card.value, [field]: value };
}
const cardStyle = computed(
  (): CSSProperties => ({
    fontSize: `${appearanceOptions.fontSize}px`,
    fontFamily: appearanceOptions.fontFamily,
    lineHeight: appearanceOptions.lineHeight,
    backgroundImage: `linear-gradient(135deg,
    color-mix(in srgb, ${appearanceOptions.backgroundColor}, white 16%),
    ${appearanceOptions.backgroundColor},
    color-mix(in srgb, ${appearanceOptions.backgroundColor}, black 12%)
  )`,
    color: appearanceOptions.color,
    border: '1px solid',
    borderColor: `color-mix(in srgb, ${appearanceOptions.backgroundColor}, black 25%)`,
    boxShadow: `
    0 0 0 1px color-mix(in srgb, color-mix(in srgb, ${appearanceOptions.backgroundColor}, black 20%), transparent 80%),
    0 2px 8px 1px color-mix(in srgb, color-mix(in srgb, ${appearanceOptions.backgroundColor}, black 25%), transparent 70%),
    10px 16px 32px -4px color-mix(in srgb, color-mix(in srgb, ${appearanceOptions.backgroundColor}, black 35%), transparent 60%),
    4px 6px 12px -2px color-mix(in srgb, color-mix(in srgb, ${appearanceOptions.backgroundColor}, black 25%), transparent 75%)
  `,
  }),
);
</script>

<template>
  <div
    class="aspect-3/2 w-full h-full flex flex-col justify-between rounded-xl transition-all duration-300 ease-out hover:-translate-y-1.5 hover:translate-x-0.5"
    :style="cardStyle"
  >
    <span class="absolute ms-auto text-xs px-5 py-3 mix-blend-difference text-white">{{
      currentSide
    }}</span>
    <div class="flex flex-col">
      <button class="absolute top-0 right-0 z-10 px-4 py-2" @click.stop="$emit('maximize')">
        <WindowIcon class="w-6 h-6 text-gray-400" />
      </button>
      <div
        :style="{
          padding: `${appearanceOptions.padding}px`,
          color: currentSide == 'back' ? appearanceOptions.accentColor : '',
        }"
      >
        <CardFront
          v-if="card"
          :term="card.term"
          :text-align="appearanceOptions.textAlign as CSSProperties['textAlign']"
        />
        <CardSkeleton v-else :appearance-options="appearanceOptions" />
      </div>
    </div>
    <div v-if="currentSide == 'back'" class="flex-1 w-full overflow-y-auto scrollbar-thin">
      <hr class="text-white mix-blend-difference" />
      <CardBack
        v-if="card"
        :definition="card.definition"
        :audio-url="card.audioUrl"
        :text-align="appearanceOptions.textAlign as CSSProperties['textAlign']"
      />
      <CardSkeleton v-else :appearance-options="appearanceOptions" />
    </div>
    <CardActions v-model="currentSide" @delete="$emit('delete')" />
  </div>
</template>
