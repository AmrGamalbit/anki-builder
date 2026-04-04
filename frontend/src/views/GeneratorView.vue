<script setup lang="ts">
import { computed, ref } from 'vue';
import GeneratorStepper from '@/components/generator/GeneratorStepper.vue';
import DeckSettings from '@/components/input/DeckSettings.vue';
import SourceInput from '@/components/generator/SourceInput.vue';
import DeckStyleEditor from '@/components/settings/DeckStyleEditor.vue';
import '@/assets/global.css';

const currentStep = ref<number>(0);
const previousDisabled = computed(() => {
  if (currentStep.value == 0) {
    return true;
  }
  return false;
});
const steps = [
  { label: 'source', component: SourceInput },
  { label: 'deck', component: DeckSettings },
  { label: 'style', component: DeckStyleEditor },
];
const payload = ref({
  source: {
    content: '',
    type: '',
  },
  deck: {
    include_pronunciation: false,
    use_dictionary_audio: false,
    include_pictures: false,
    mode: 'definition',
    source: 'dictionary',
    provider: 'free_dictionary_api',
  },
  style: {
    font_family: `'Segoe UI', sans-serif`,
    font_size: 16,
    line_height: 1.4,
    padding: 20,
    text_align: 'center',
    accent_color: 'blue',
    background_color: '#ffffff',
    color: '#1a1a1a',
    night_mode: true,
  },
});

const text = computed(() => {
  if (currentStep.value < 2) {
    return 'Next';
  }
  return 'Generate';
});

function onNext() {
  if (currentStep.value < 2) {
    currentStep.value++;
  } else {
    generate();
  }
}

function generate() {
  console.log(payload.value);
}
</script>

<template>
  <section class="p-20 flex flex-col min-h-screen justify-between">
    <component :is="steps[currentStep].component" v-model="payload[steps[currentStep].label]" />
    <div>
      <div class="flex justify-between mb-5">
        <button
          class="bg-primary text-surface rounded p-2 cursor-pointer disabled:bg-gray-300"
          @click="currentStep--"
          :disabled="previousDisabled"
        >
          Previous
        </button>
        <button class="bg-primary text-surface rounded p-2 cursor-pointer" @click="onNext">
          {{ text }}
        </button>
      </div>
      <GeneratorStepper class="mt-auto" v-model="currentStep" />
    </div>
  </section>
</template>
