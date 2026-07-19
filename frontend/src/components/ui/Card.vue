<script setup lang="ts">
import { useGeneratorStore } from '@/stores/generator';
import { ArrowsRightLeftIcon } from '@heroicons/vue/16/solid';
import { ref, computed } from 'vue';
import type { CSSProperties } from 'vue';
import { PencilSquareIcon, PlayCircleIcon, WindowIcon, TrashIcon } from '@heroicons/vue/16/solid';
import type { CardData } from '@/types/card';
import CardSkeleton from './CardSkeleton.vue';

const emit = defineEmits<{ maximize: []; delete: [] }>();
const card = defineModel<CardData | null>('card');
const generatorStore = useGeneratorStore();
const appearanceOptions = generatorStore.appearanceOptions;
const currentSide = ref('front');
const audioRef = ref<HTMLAudioElement | null>(null);
const flipCard = () => {
  currentSide.value == 'front' ? (currentSide.value = 'back') : (currentSide.value = 'front');
};
const handlePencilClick = (event: MouseEvent) => {
  const textEl = (event.currentTarget as HTMLElement).previousElementSibling;
  (textEl as HTMLElement)?.focus();
};
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
    <div class="flex flex-col overflow-hidden">
      <button class="absolute top-0 right-0 z-10 px-4 py-2" @click.stop="$emit('maximize')">
        <WindowIcon class="w-6 h-6 text-gray-400" />
      </button>
      <div
        :style="{
          padding: `${appearanceOptions.padding}px`,
          color: currentSide == 'back' ? appearanceOptions.accentColor : '',
        }"
      >
        <div class="group relative" v-if="card">
          <input
            class="w-full bg-transparent border-none outline-none cursor-text p-2 hover:ring-1 hover:ring-dashed hover:ring-gray-400 rounded transition-all placeholder:text-gray-400 placeholder:italic"
            :style="{ textAlign: appearanceOptions.textAlign as CSSProperties['textAlign'] }"
            placeholder="Enter term..."
            @change="handleUpdateCard(($event.target as HTMLInputElement).value, 'term')"
            :value="card.term"
            @click.stop
          />
          <PencilSquareIcon
            class="w-6 h-6 absolute top-0 right-0 mx-1 opacity-0 group-hover:opacity-100 transition-opacity text-gray-400 cursor-pointer"
            @click.stop="handlePencilClick"
          />
        </div>
        <CardSkeleton v-else :appearance-options="appearanceOptions" />
      </div>
    </div>
    <div v-if="currentSide == 'back'" class="flex-1">
      <hr class="text-white mix-blend-difference" />
      <div v-if="card">
        <div class="group relative overflow-y-auto scrollbar-thin">
          <textarea
            class="w-full bg-transparent border-none outline-none cursor-text p-2 hover:ring-1 hover:ring-gray-400 rounded resize-none transition-all placeholder:text-gray-400 placeholder:italic"
            :style="{ textAlign: appearanceOptions.textAlign as CSSProperties['textAlign'] }"
            :value="card.definition"
            @change="handleUpdateCard(($event.target as HTMLInputElement).value, 'definition')"
            placeholder="Enter definition..."
            @click.stop
          />
          <PencilSquareIcon
            class="w-6 h-6 absolute top-0 right-0 m-1 opacity-0 group-hover:opacity-100 transition-opacity text-gray-400 cursor-pointer"
            @click.stop="handlePencilClick"
          />
        </div>
        <div v-if="card?.audioUrl">
          <audio controls :src="card?.audioUrl" class="hidden" ref="audioRef"></audio>
          <button @click.stop="audioRef?.play()">
            <PlayCircleIcon class="w-6 h-6" />
          </button>
        </div>
      </div>
      <CardSkeleton v-else :appearance-options="appearanceOptions" />
    </div>
    <div class="p-5 mx-auto mix-blend-difference">
      <ArrowsRightLeftIcon
        class="w-7 h-7 block cursor-pointer text-black bg-white rounded-4xl p-0.5"
        @click.stop="flipCard"
      />
    </div>
    <button
      class="flex items-center justify-center cursor-pointer rounded-b-lg p-2 text-gray-400 transition-colors hover:bg-red-50 hover:text-red-600"
      @click.stop="$emit('delete')"
    >
      <TrashIcon class="h-5 w-5" />
    </button>
  </div>
</template>
