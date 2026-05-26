<script setup lang="ts">
import { computed, watchEffect } from 'vue';
import OptionField from '../ui/OptionField.vue';
import LanguagePairSelector from './deck/LanguagePairSelector.vue';
import type { OptionItem, DeckOptions } from '@/types/option';
import type { SchemaField } from '@/types/schema';

type ProviderKey = 'dictionary' | 'ai';
const providers: Record<ProviderKey, OptionItem[]> = {
  dictionary: [{ label: 'Free Dictionary API', value: 'free_dictionary_api' }],
  ai: [
    { label: 'Gemini', value: 'gemini' },
    { label: 'Groq', value: 'groq' },
  ],
};

const deckOptions = defineModel<DeckOptions>({
  default: {
    include_pronunciation: false,
    include_pictogram: false,
    source: 'ai',
    provider: 'groq',
  },
});

const deckSchema = computed<Record<string, SchemaField>>(() => {
  return {
    include_pronunciation: {
      label: 'Include Pronunciation',
      type: 'boolean',
    },
    include_pictogram: {
      label: 'Include Pictograms',
      type: 'boolean',
    },
    source: {
      label: 'Source',
      type: 'select',
      items: [
        { label: 'Dictionary', value: 'dictionary' },
        { label: 'AI', value: 'ai' },
      ],
    },
    provider: {
      label: 'Provider',
      type: 'select',
      items: providers[deckOptions.value.source as ProviderKey],
    },
    mode: {
      label: 'Mode',
      type: 'select',
      items: [
        { label: 'Definition', value: 'definition' },
        { label: 'Translation', value: 'translation' },
      ],
      shouldShow: deckOptions.value.source == 'ai',
    },
    use_dictionary_audio: {
      label: 'Use Dictionary Audio',
      type: 'boolean',
      shouldShow:
        deckOptions.value.include_pronunciation == true && deckOptions.value.source == 'dictionary',
    },
  };
});

const visibleDeckSchema = computed(() =>
  Object.fromEntries(
    Object.entries(deckSchema.value).filter(([_, option]) => option?.shouldShow !== false),
  ),
);
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Deck</h2>
    <hr class="m-5" />
    <div class="flex flex-col gap-5">
      <LanguagePairSelector
        v-model:sourceLanguage="deckOptions['source_language']"
        v-model:targetLanguage="deckOptions['target_language']"
      />
      <OptionField
        v-for="(option, key) in visibleDeckSchema"
        :key="key"
        :option="option"
        v-model="deckOptions[key as keyof typeof deckOptions]"
      />
      <div class="flex justify-between items-center">
        <h2 class="text-gray-900 dark:text-gray-100">Deck Name</h2>
        <div class="w-48 max-w-sm min-w-[200px]">
          <input
            class="inline-flex h-9 w-48 bg-white placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
            placeholder="Type here..."
            v-model="deckOptions.deck_name"
          />
        </div>
      </div>
    </div>
  </section>
</template>
