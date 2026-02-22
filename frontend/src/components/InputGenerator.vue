<script setup lang="ts">
import SourceOptions from '@/components/GeneratorSourceOptions.vue';
import FormatOptions from '@/components/GeneratorFormatOptions.vue';
import FileInput from '@/components/FileInput.vue';
import SingleWordInput from '@/components/WordInput.vue';
import TextInput from '@/components/TextInput.vue';

import { ref } from 'vue';

const content = defineModel();
const formData = new FormData();
const type = ref('');
const selectedSource = ref(1);

async function handleSubmit() {
  formData.append('data', {
    type: type.value,
    include_pronunciation: false,
    include_photos: false,
    definition_source: 'ai',
  });

  if (selectedSource == 0 || selectedSource == 1) {
    type.value = 'text';
    form.data.append('text', content.value.split(','));
  } else {
    type.value = 'file';
    formData.append('file', content.value);
  }

  const response = await fetch('http://127.0.0.1:8000/generate-deck', {
    method: 'POST',
    body: formData,
    headers: {
      'Content-type': 'multipart/form-data',
    },
  });
  const data = await response.json();
}
</script>

<template>
  <section class="p-20 bg-gray-50 text-neutral font-koho">
    <h2 class="text-4xl font-semibold">Input</h2>
    <form action="" class="mt-10">
      <SourceOptions @selectSource="(active) => (selectedSource = active)" />
      <SingleWordInput v-if="selectedSource == 0" v-model="content" />
      <TextInput v-else-if="selectedSource == 1" v-model="content" />
      <FileInput v-else v-model="content" />
      <FormatOptions />
      <button
        type="submit"
        class="bg-primary text-surface font-semibold p-2 rounded-sm cursor-pointer block ml-auto mt-10"
        @click.prevent="handleSubmit"
      >
        Generate Anki Deck
      </button>
    </form>
  </section>
</template>
<!--
<style scoped>
.deck-generator {
  margin: 20px;
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-secondary);
  padding: 50px;
  color: var(--primary-color);
  display: flex;
  flex-direction: column;
  gap: 10px;
  border-radius: 10px;
  width: 100%;
  height: 80vh;
}

.deck-generator__form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

#deck-generator__input {
  width: 100%;
  height: 100px;
  border-radius: 10px;
}

button {
  background-color: var(--button-primary);
  color: var(--color-primary);
  font-family: inherit;
  font-size: inherit;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-weight: bold;
  cursor: pointer;
}
</style> -->
