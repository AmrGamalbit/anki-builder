<script setup lang="ts">
import { useGeneratorStore } from '@/stores/generator';
import { ArrowsRightLeftIcon, ArrowPathIcon } from '@heroicons/vue/16/solid';
import { ref } from 'vue';
import type { CSSProperties } from 'vue';
import { PencilSquareIcon } from '@heroicons/vue/16/solid';
import type { CardData } from '@/types/card';

const card = defineModel<CardData | null>('card');
const generatorStore = useGeneratorStore();
const appearanceOptions = generatorStore.appearanceOptions;
const currentSide = ref('front');
const flipCard = () => {
  currentSide.value == 'front' ? (currentSide.value = 'back') : (currentSide.value = 'front');
};
const handlePencilClick = (event: MouseEvent) => {
  const textEl = (event.currentTarget as HTMLElement).previousElementSibling;
  (textEl as HTMLElement)?.focus();
};
function handleCardUpdate(event: FocusEvent, field: 'front' | 'back') {
  if (!card.value) return;
  card.value = { ...card.value, [field]: (event.target as HTMLElement).innerText };
}
</script>

<template>
  <div
    class="aspect-3/2 flex flex-col justify-between overflow-hidden rounded-xl transition-all duration-300 ease-out hover:-translate-y-1.5 hover:translate-x-0.5"
    :style="
      {
        fontSize: `${appearanceOptions.fontSize}px`,
        fontFamily: appearanceOptions.fontFamily,
        textAlign: appearanceOptions.textAlign,
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
      } as CSSProperties
    "
  >
    <span class="absolute ms-auto text-xs px-5 py-3 mix-blend-difference text-white">{{
      currentSide
    }}</span>
    <div class="flex flex-col">
      <div
        :style="{
          padding: `${appearanceOptions.padding}px`,
          color: currentSide == 'back' ? appearanceOptions.accentColor : '',
        }"
      >
        <div class="group relative" v-if="card?.front">
          <p
            class="cursor-text border border-transparent hover:border-dashed hover:border-gray-400 rounded transition-colors"
            contenteditable="true"
            @blur="handleCardUpdate($event, 'front')"
            @click.stop
          >
            {{ card?.front }}
          </p>
          <PencilSquareIcon
            class="w-6 h-6 absolute top-0 right-0 mx-1 opacity-0 group-hover:opacity-100 transition-opacity text-gray-400 cursor-pointer"
            @click.stop="handlePencilClick"
          />
        </div>
        <ArrowPathIcon class="w-6 h-6 animate-spin mx-auto" v-else />
      </div>
      <div v-if="currentSide == 'back'" class="flex-1">
        <hr class="text-white mix-blend-difference" />
        <div class="group relative" v-if="card?.back">
          <p
            class="p-2 cursor-text border border-transparent hover:border-dashed hover:border-gray-400 rounded transition-colors"
            contenteditable="true"
            @blur="handleCardUpdate($event, 'back')"
            @click.stop
          >
            {{ card?.back }}
          </p>
          <PencilSquareIcon
            class="w-6 h-6 absolute top-0 right-0 m-1 opacity-0 group-hover:opacity-100 transition-opacity text-gray-400 cursor-pointer"
            @click.stop="handlePencilClick"
          />
        </div>
        <ArrowPathIcon class="w-6 h-6 animate-spin mx-auto m-2" v-else />
      </div>
    </div>
    <div class="p-5 mx-auto mix-blend-difference">
      <ArrowsRightLeftIcon
        class="w-7 h-7 block cursor-pointer text-black bg-white rounded-4xl p-0.5"
        @click.stop="flipCard"
      />
    </div>
  </div>
</template>
