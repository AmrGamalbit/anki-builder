<script setup lang="ts">
import ApiKeyInput from '../ui/ApiKeyInput.vue';

const providers = [
  { label: 'Groq', key: 'groq' },
  { label: 'Gemini', key: 'gemini' },
  { label: 'Wordnik', key: 'wordnik' },
];
</script>

<template>
  <h2 class="text-3xl text-neutral mb-10 font-medium">API Keys</h2>
  <div class="grid grid-cols-2 gap-4">
    <ApiKeyInput
      v-for="provider in providers"
      :label="provider.label"
      :key="provider.label"
      v-model="provider.key"
    />
  </div>
</template>
