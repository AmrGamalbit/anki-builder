<script setup lang="ts">
import OptionRow from '@/components/ui/OptionRow.vue';

const model = defineModel();
model.value.options = { type: 'text' };

const options = {
  delimiter: {
    label: 'Delimiter',
    type: 'select',
    items: [
      { label: 'Newline', value: '\n' },
      { label: 'Comma', value: ',' },
      { label: 'Space', value: ' ' },
    ],
  },
  strip_punctuation: { label: 'Strip Punctuation', type: 'boolean' },
  lowercase: { label: 'All Lowercase', type: 'boolean' },
  base_form: { label: 'Base Form Only', type: 'boolean' },
};
</script>

<template>
  <div>
    <label for="deck-generator__input" class="sr-only">Place your words, separated by commas</label>
    <textarea
      name="Words Input"
      id="deck-generator__input"
      class="bg-white dark:text-gray-900 w-full h-50 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2"
      placeholder="Place your words, separated by commas"
      v-model="model.content"
    ></textarea>
  </div>
  <div class="flex flex-col gap-5">
    <OptionRow
      v-for="(option, key) in options"
      :option="option"
      :key="key"
      v-model="model.options[key]"
    />
  </div>
</template>
