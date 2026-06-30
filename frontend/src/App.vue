<script setup lang="ts">
import Navbar from '@/components/Navbar.vue';
import { onMounted } from 'vue';
import { RouterView } from 'vue-router';
import { syncApiKeys } from './api/auth';
import '@/assets/global.css';

onMounted(async () => {
  await syncApiKeys();
});
</script>

<template>
  <Navbar />
  <RouterView />
</template>

<style scoped>
.wrapper {
  display: flex;
  justify-content: space-between;
}
</style>
