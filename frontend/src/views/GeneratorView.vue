<script setup lang="ts">
import InputGenerator from '@/components/InputGenerator.vue';
import '@/assets/global.css';
</script>

<template>
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
