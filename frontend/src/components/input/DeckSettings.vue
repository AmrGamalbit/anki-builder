<script setup lang="ts">
import { ref, computed } from 'vue';
import OptionRow from '../ui/OptionRow.vue';

const providers = {
  dictionary: [{ label: 'Free Dictionary API', value: 'freeDictionaryAPI' }],
  ai: [
    { label: 'Gemini', value: 'gemini' },
    { label: 'Groq', value: 'groq' },
  ],
};

const optionValues = defineModel();

const options = {
  include_pronunciation: {
    label: 'Include Pronunciation',
    type: 'boolean',
  },
  include_pictures: {
    label: 'Include Pictures',
    type: 'boolean',
  },
  mode: {
    label: 'Mode',
    type: 'select',
    items: [
      { label: 'Definition', value: 'definition' },
      { label: 'Translation', value: 'translation' },
    ],
  },
  source: {
    label: 'Source',
    type: 'select',
    items: [
      { label: 'Dictionary', value: 'dictionary' },
      { label: 'AI', value: 'ai' },
    ],
  },
};
const sourceProvider = computed(() => ({
  label: 'Provider',
  type: 'select',
  items: providers[optionValues.value.source],
}));
</script>

<template>
  <h2 class="text-lg font-semibold text-slate-900 border-b pb-2 mb-4">Settings</h2>
  <div class="flex flex-col gap-5">
    <OptionRow
      v-for="(option, key) in options"
      :key="key"
      :option="option"
      v-model="optionValues[key]"
    />
    <OptionRow :option="sourceProvider" />
  </div>
</template>
