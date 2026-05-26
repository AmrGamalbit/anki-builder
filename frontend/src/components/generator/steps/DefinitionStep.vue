<script setup lang="ts">
import { computed } from 'vue';
import OptionField from '@/components/ui/OptionField.vue';
import LanguagePairSelector from '@/components/generator/deck/LanguagePairSelector.vue';
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
    <h2 class="text-4xl text-neutral font-medium">Definition</h2>
    <hr class="m-5" />
    <div class="flex flex-col gap-5">
      <LanguagePairSelector
        v-model:sourceLanguage="deckOptions['source_language']"
        v-model:targetLanguage="deckOptions['target_language']"
      />
      <div class="flex flex-col gap-4">
        <OptionField
          v-for="(option, key) in visibleDeckSchema"
          :key="key"
          :option="option"
          v-model="deckOptions[key as keyof typeof deckOptions]"
        />
      </div>
    </div>
  </section>
</template>
