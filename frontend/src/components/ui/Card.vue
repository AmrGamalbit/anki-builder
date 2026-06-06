<script setup lang="ts">
import { useGeneratorStore } from '@/stores/generator';
import { ArrowsRightLeftIcon } from '@heroicons/vue/16/solid';
import { ref } from 'vue';
import type { CSSProperties } from 'vue';

interface Flashcard {
  front: string;
  back: string | null;
}
const generatorStore = useGeneratorStore();
const appearanceOptions = generatorStore.appearanceOptions;
const currentSide = ref('front');
const props = defineProps<{ card: Flashcard }>();
const flipCard = () => {
  currentSide.value == 'front' ? (currentSide.value = 'back') : (currentSide.value = 'front');
};
</script>

<template>
  <div
    class="aspect-3/2 flex flex-col justify-between relative overflow-hidden rounded-xl transition-all duration-300 ease-out hover:-translate-y-1.5 hover:translate-x-0.5"
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
      <p
        :style="{
          padding: `${appearanceOptions.padding}px`,
          color: currentSide == 'back' ? appearanceOptions.accentColor : '',
        }"
      >
        {{ props.card.front }}
      </p>
      <div v-if="currentSide == 'back'" class="flex-1">
        <hr class="text-white mix-blend-difference" />
        <p class="p-2">{{ props.card.back }}</p>
      </div>
    </div>
    <div class="p-5 mx-auto mix-blend-difference">
      <ArrowsRightLeftIcon
        class="w-7 h-7 block cursor-pointer text-black bg-white rounded-4xl p-0.5"
        @click="flipCard"
      />
    </div>
  </div>
</template>
