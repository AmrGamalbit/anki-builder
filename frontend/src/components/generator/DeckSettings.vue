<script setup lang="ts">
import { ref, computed, watchEffect } from 'vue';
import OptionRow from '../ui/OptionRow.vue';
import LanguagePairSelector from './deck/LanguagePairSelector.vue';

const providers = {
  dictionary: [{ label: 'Free Dictionary API', value: 'free_dictionary_api' }],
  ai: [
    { label: 'Gemini', value: 'gemini' },
    { label: 'Groq', value: 'groq' },
  ],
};

const optionValues = defineModel();

const options = ref({
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
});
const sourceProvider = computed(() => ({
  label: 'Provider',
  type: 'select',
  items: providers[optionValues.value.source],
}));

watchEffect(() => {
  const v = optionValues.value;

  const shouldShow = {
    use_dictionary_audio: v.include_pronunciation && v.source === 'dictionary',
    mode: v.source === 'ai',
  };

  if (shouldShow.use_dictionary_audio) {
    options.value.use_dictionary_audio = { label: 'Use Dictionary Audio', type: 'boolean' };
  } else {
    delete options.value.use_dictionary_audio;
  }

  if (shouldShow.mode) {
    options.value.mode = {
      label: 'Mode',
      type: 'select',
      items: [
        { label: 'Definition', value: 'definition' },
        { label: 'Translation', value: 'translation' },
      ],
    };
  } else {
    delete options.value.mode;
  }
});
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Deck</h2>
    <hr class="m-5" />
    <div class="flex flex-col gap-5">
      <LanguagePairSelector
        v-model:sourceLanguage="optionValues['source_language']"
        v-model:targetLanguage="optionValues['target_language']"
      />
      <OptionRow
        v-for="(option, key) in options"
        :key="key"
        :option="option"
        v-model="optionValues[key]"
      />
      <OptionRow :option="sourceProvider" v-model="optionValues['provider']" />
    </div>
  </section>
</template>
