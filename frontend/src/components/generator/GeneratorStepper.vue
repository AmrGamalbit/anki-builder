<script setup lang="ts">
import { computed, ref } from 'vue';
import SetupStep from '@/components/generator/steps/SetupStep.vue';
import ContentStep from '@/components/generator/steps/ContentStep.vue';
import AppearanceStep from '@/components/generator/steps/AppearanceStep.vue';
import ReviewStep from '@/components/generator/steps/ReviewStep.vue';
import DefinitionStep from './steps/DefinitionStep.vue';

const currentStep = ref(0);
const emit = defineEmits(['complete']);
const buttonText = computed(() => {
  return currentStep.value < 4 ? 'Next' : 'Generate';
});

function onNext() {
  currentStep.value < 4 ? currentStep.value++ : emit('complete');
}
const steps = [SetupStep, ContentStep, DefinitionStep, AppearanceStep, ReviewStep];
</script>

<template>
  <section class="p-5 md:p-20 flex flex-col min-h-screen justify-between">
    <component :is="steps[currentStep]" />
    <div class="flex flex-col justify-around">
      <div>
        <div class="flex justify-between mb-5">
          <button
            class="bg-primary text-neutral rounded p-2 cursor-pointer disabled:bg-gray-300 disabled:text-gray-900"
            @click="currentStep--"
            :disabled="currentStep == 0"
          >
            Previous
          </button>
          <button class="bg-primary text-neutral rounded p-2 cursor-pointer" @click="onNext">
            {{ buttonText }}
          </button>
        </div>
      </div>
      <div class="w-full">
        <div class="relative flex items-center justify-between w-full">
          <div class="absolute left-0 top-2/4 h-0.5 w-full -translate-y-2/4 bg-gray-300"></div>
          <div
            class="absolute left-0 top-2/4 h-0.5 w-full -translate-y-2/4 bg-gray-900 transition-all duration-500"
          ></div>
          <div
            v-for="step in 5"
            class="relative z-10 grid w-10 h-10 font-bold text-gray-900 transition-all duration-300 bg-gray-300 rounded-full place-items-center"
            :class="currentStep + 1 == step ? 'bg-gray-900 text-white' : ''"
          >
            {{ step }}
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
