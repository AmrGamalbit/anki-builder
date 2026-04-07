<script setup lang="ts">
import { computed, ref } from 'vue';
import GeneratorStepper from '@/components/generator/GeneratorStepper.vue';
import DeckSettings from '@/components/input/DeckSettings.vue';
import SourceInput from '@/components/generator/SourceInput.vue';
import DeckStyleEditor from '@/components/settings/DeckStyleEditor.vue';
import Alert from '@/components/ui/BaseAlert.vue';
import Modal from '@/components/ui/BaseModal.vue';
import { useApi } from '@/composables/useApi';
import '@/assets/global.css';

const currentStep = ref<number>(0);
const alertIntent = ref<string>('success');
const showModal = ref<boolean>(false);
const showAlert = ref<boolean>(false);
const alertMessage = ref<string>('');
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
    include_pictogram: false,
    mode: 'definition',
    source: 'dictionary',
    provider: 'free_dictionary_api',
    source_language: 'en',
    target_language: 'en',
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

const { getEndpoint } = useApi();

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

async function generate() {
  showModal.value = true;
  const endpoint = getEndpoint(payload.value.deck.source, payload.value.source.type);
  if (payload.value.source.type != 'file') {
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload.value),
    });
    // const r = await response.json();
    if (!response.ok) {
      alertIntent.value = 'danger';
      alertMessage.value = 'Something went wrong';
    } else {
      alertMessage.value = 'Deck was generated successfully';
    }
    showAlert.value = true;
    showModal.value = false;
  }
}
</script>

<template>
  <section class="p-5 md:p-20 flex flex-col min-h-screen justify-between">
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
  <Modal :isOpen="showModal">
    <WrenchIcon class="w-6 h-6 m-2" />
    <h2 class="text-xl font-semibold">Hold Tight!</h2>
    <p>Your deck is being <span class="text-green-900 font-semibold">generated</span> right now</p>
  </Modal>
  <Alert :intent="alertIntent" :title="alertMessage" v-model="showAlert" />
</template>
