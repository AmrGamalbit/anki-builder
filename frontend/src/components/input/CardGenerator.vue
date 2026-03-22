<script setup lang="ts">
import SourceOptions from './SourceInput.vue';
import DeckSettings from './DeckSettings.vue';
import LanguagePairSelector from './LanguagePairSelector.vue';

import { ref } from 'vue';
import { useApi } from '@/composables/useApi';

const selectedSource = ref<number>(1);
const content = ref<string>();
const type = ref<string>();
const deckSettings = ref({
  include_pronunciation: false,
  use_dictionary_audio: false,
  include_pictures: false,
  mode: 'definition',
  source: 'dictionary',
  provider: 'free_dictionary_api',
});
const languagePair = ref({
  source_language: 'en',
  target_language: 'en',
});

const { getEndpoint, buildPayload } = useApi();

async function handleSubmit() {
  const data = { ...deckSettings.value, ...languagePair.value, content: content.value };
  selectedSource.value == 2 ? (type.value = 'file') : (type.value = 'text');

  const endpoint = getEndpoint(data.source, type.value);
  const payload = buildPayload(data, type.value);

  if (type.value == 'file') {
    const response = await fetch(endpoint, {
      method: 'POST',
      body: payload,
    });
    const r = await response.json();
    console.log(r);
  } else {
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const r = await response.json();
    console.log(r);
  }
}
</script>

<template>
  <section class="p-10 md:p-16 bg-surface text-neutral font-koho">
    <h2 class="text-4xl font-semibold">Input</h2>
    <form action="" class="mt-10">
      <SourceOptions v-model:content="content" v-model:selectedSource="selectedSource" />
      <LanguagePairSelector v-model="languagePair" />
      <DeckSettings v-model="deckSettings" />
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
