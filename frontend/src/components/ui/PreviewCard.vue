<script setup lang="ts">
import { useGeneratorStore } from '@/stores/generator';
import { ArrowsRightLeftIcon } from '@heroicons/vue/16/solid';
import { ref } from 'vue';
import type { CSSProperties } from 'vue';

const generatorStore = useGeneratorStore();
const appearanceOptions = generatorStore.appearanceOptions;
const currentSide = ref('front');
const card = {
  front: 'Hello',
  back: 'A greeting used to express affection',
};
const flipCard = () => {
  currentSide.value == 'front' ? (currentSide.value = 'back') : (currentSide.value = 'front');
};
</script>

<template>
  <div
    class="ring-2 ring-gray-600 rounded-lg overflow-hidden relative aspect-3/2 flex flex-col justify-between"
    :style="
      {
        fontSize: `${appearanceOptions.fontSize}px`,
        fontFamily: appearanceOptions.fontFamily,
        textAlign: appearanceOptions.textAlign,
        lineHeight: appearanceOptions.lineHeight,
        backgroundColor: appearanceOptions.backgroundColor,
        color: appearanceOptions.color,
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
        {{ card.front }}
      </p>
      <div v-if="currentSide == 'back'" class="flex-1">
        <hr class="text-white" />
        <p class="p-2">{{ card.back }}</p>
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
