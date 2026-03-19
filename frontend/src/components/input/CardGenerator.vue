<script setup lang="ts">
import SourceOptions from './SourceInput.vue';
import DeckSettings from './DeckSettings.vue';

import LanguagePairSelector from './LanguagePairSelector.vue';

import { ref } from 'vue';

const selectedSource = ref<number>(1);
const content = ref<string>();
const formData = new FormData();
const type = ref<string>();
const settings = ref({
  include_pronunciation: false,
  include_pictures: false,
  mode: 'definition',
  source: 'dictionary',
  provider: 'freeDictionaryAPI',
});
const languagePair = ref({
  source_language: 'en',
  target_language: 'en',
});

async function handleSubmit() {
  if (selectedSource.value == 0 || selectedSource.value == 1) {
    type.value = 'text';
    formData.append('content', content.value);
  } else {
    type.value = 'file';
    formData.append('file', content.value);
  }
  const payload = {
    ...languagePair.value,
    ...settings.value,
  };

  for (const key in payload) {
    formData.append(key, payload[key as keyof typeof payload]);
  }

  const response = await fetch('http://127.0.0.1:8000/generate-deck', {
    method: 'POST',
    body: formData,
  });
  const data = await response.json();
}
</script>

<template>
  <section class="p-20 bg-surface text-neutral font-koho">
    <h2 class="text-4xl font-semibold">Input</h2>
    <form action="" class="mt-10">
      <SourceOptions v-model:content="content" v-model:selectedSource="selectedSource" />
      <LanguagePairSelector v-model="languagePair" />
      <DeckSettings v-model="settings" />
      <button
        type="submit"
        class="bg-primary-muted text-surface dark:text-white font-semibold p-2 rounded-sm cursor-pointer block ml-auto mt-10"
        @click.prevent="handleSubmit"
      >
        Generate Anki Deck
      </button>
    </form>
  </section>
</template>
