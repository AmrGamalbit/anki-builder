<script setup lang="ts">
import { ref } from 'vue';
import { WrenchIcon } from '@heroicons/vue/16/solid';
import GeneratorStepper from '@/components/generator/GeneratorStepper.vue';
import Alert from '@/components/ui/Alert.vue';
import Modal from '@/components/ui/Modal.vue';
import { generateDeck } from '@/api/generator';
import '@/assets/global.css';

type Intent = 'danger' | 'success' | 'info' | 'warning';
const alertIntent = ref<Intent>('success');
const showModal = ref(false);
const showAlert = ref(false);
const alertMessage = ref('');
async function handleGenerate() {
  showModal.value = true;
  const { intent, msg } = await generateDeck();
  alertIntent.value = intent as Intent;
  alertMessage.value = msg;
  showModal.value = false;
  showAlert.value = true;
}
</script>

<template>
  <GeneratorStepper @complete="handleGenerate" />
  <Modal :isOpen="showModal">
    <WrenchIcon class="w-6 h-6 m-2" />
    <h2 class="text-xl font-semibold">Hold Tight!</h2>
    <p>Your deck is being <span class="text-green-900 font-semibold">generated</span> right now</p>
  </Modal>
  <Alert :intent="alertIntent" :title="alertMessage" v-model="showAlert" />
</template>
