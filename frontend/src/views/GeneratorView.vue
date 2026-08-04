<script setup lang="ts">
import { ref } from 'vue';
import { WrenchIcon } from '@heroicons/vue/16/solid';
import GeneratorStepper from '@/components/generator/GeneratorStepper.vue';
import Alert from '@/components/ui/Alert.vue';
import Modal from '@/components/ui/Modal.vue';
import { generateDeck, triggerDownload } from '@/api/generator';
import '@/assets/global.css';

type Intent = 'danger' | 'success' | 'info' | 'warning';
const showModal = ref(false);
const alertIntent = ref<Intent>('success');
const alertMessage = ref<string | null>('');
async function handleGenerate() {
  try {
    await generateDeck();
    alertMessage.value = 'Deck Generated!';
    alertIntent.value = 'success';
  } catch (e: any) {
    alertMessage.value = e.message;
    alertIntent.value = 'danger';
  }
}
async function handleExport() {
  try {
    await triggerDownload();
    alertMessage.value = 'Deck Export Complete!';
    alertIntent.value = 'success';
  } catch (e: any) {
    alertMessage.value = e.message;
    alertIntent.value = 'danger';
  }
}
</script>

<template>
  <GeneratorStepper @generate-requested="handleGenerate" @export-requested="handleExport" />
  <Modal v-model="showModal">
    <WrenchIcon class="w-6 h-6 m-2" />
    <h2 class="text-xl font-semibold">Hold Tight!</h2>
    <p>Your deck is being <span class="text-green-900 font-semibold">generated</span> right now</p>
  </Modal>
  <Alert
    v-if="alertMessage"
    :intent="alertIntent"
    :title="alertMessage"
    @close="alertMessage = null"
  />
</template>
