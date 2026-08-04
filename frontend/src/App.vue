<script setup lang="ts">
import Navbar from '@/components/Navbar.vue';
import { onMounted, ref } from 'vue';
import { RouterView } from 'vue-router';
import { syncApiKeys } from './api/auth';
import '@/assets/global.css';
import Alert from './components/ui/Alert.vue';

type Intent = 'danger' | 'success' | 'info' | 'warning';
const alertMessage = ref<string | null>();
const alertIntent = ref<Intent>('success');
onMounted(async () => {
  try {
    alertMessage.value = await syncApiKeys();
    alertIntent.value = 'success'
  } catch (e: any) {
    alertMessage.value = e.message;
    alertIntent.value = 'danger'
  }
});
</script>

<template>
  <Navbar />
  <RouterView />
  <Alert v-if="alertMessage" :intent="alertIntent" :title="alertMessage" @close="alertMessage = null" />
</template>

<style scoped>
.wrapper {
  display: flex;
  justify-content: space-between;
}
</style>
