<script setup lang="ts">
import Navbar from '@/components/navbar/Navbar.vue';
import { RouterView } from 'vue-router';
import '@/assets/global.css';
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
