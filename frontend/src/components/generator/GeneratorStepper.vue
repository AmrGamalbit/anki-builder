<script setup lang="ts">
import { computed, ref } from 'vue';
import ContentStep from '@/components/generator/steps/ContentStep.vue';
import DefinitionStep from './steps/DefinitionStep.vue';
import AppearanceStep from '@/components/generator/steps/AppearanceStep.vue';
import ReviewStep from '@/components/generator/steps/ReviewStep.vue';
import { useGeneratorStore } from '@/stores/generator.ts';

const emit = defineEmits(['generate-requested', 'export-requested']);
const generatorStore = useGeneratorStore();
const steps = [ContentStep, DefinitionStep, AppearanceStep, ReviewStep];
const currentStep = ref(0);
const buttonText = computed(() => {
  switch (currentStep.value) {
    case 2:
      return 'Generate';
    case 3:
      return 'Export';
    default:
      return 'Next';
  }
});
const canProceed = computed(() => {
  switch (currentStep.value) {
    case 2:
      return generatorStore.content;
    case 3:
      return generatorStore.cards.length > 0;
    default:
      return true;
  }
});
function onNext() {
  if (!canProceed.value) return;
  switch (currentStep.value) {
    case 2:
      emit('generate-requested');
      break;
    case 3:
      emit('export-requested');
      break;
  }
  currentStep.value++;
}
</script>

<template>
  <section class="p-5 md:p-20 flex flex-col min-h-screen justify-between">
    <component :is="steps[currentStep]" />
    <div class="flex flex-col justify-around">
      <div>
        <div class="flex justify-between mb-5">
          <button
            class="bg-primary text-gray-200 rounded p-2 cursor-pointer disabled:bg-gray-300 disabled:text-gray-900 disabled:cursor-not-allowed"
            @click="currentStep--"
            :disabled="currentStep == 0"
          >
            Previous
          </button>
          <button
            class="bg-primary text-gray-200 rounded p-2 cursor-pointer disabled:bg-gray-300 disabled:text-gray-900 disabled:cursor-not-allowed"
            @click="onNext"
            :disabled="!canProceed"
          >
            {{ buttonText }}
          </button>
        </div>
      </div>
      <div class="w-full">
        <div class="relative flex items-center justify-between w-full">
          <div class="absolute left-0 top-2/4 h-0.5 w-full -translate-y-2/4 bg-gray-300"></div>
          <div
            class="absolute left-0 top-2/4 h-0.5 w-full -translate-y-2/4 bg-gray-900 transition-all duration-500"
            :style="{ width: `${(currentStep / (steps.length - 1)) * 100}%` }"
          ></div>
          <div
            v-for="(step, index) in steps"
            @click="currentStep = index"
            class="relative z-10 grid w-10 h-10 font-bold text-gray-900 transition-all duration-300 bg-gray-300 rounded-full place-items-center cursor-pointer"
            :class="
              index < currentStep
                ? 'bg-gray-900 text-white'
                : index === currentStep
                  ? 'bg-gray-700 text-white'
                  : 'bg-gray-300 text-gray-900'
            "
          >
            {{ index + 1 }}
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
