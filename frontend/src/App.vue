<script setup lang="ts">
import Navbar from '@/components/Navbar.vue';
import InputGenerator from '@/components/InputGenerator.vue';
import '@/assets/global.css';
</script>

<template>
  <Navbar />
  <div class="wrapper">
    <InputGenerator />
    <InputGenerator />
  </div>
</template>

<style scoped>
.wrapper {
    display: flex;
    justify-content: space-between;
}
</style>
