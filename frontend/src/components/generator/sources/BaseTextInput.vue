<script setup lang="ts">
import OptionRow from '@/components/ui/OptionField.vue';

const model = defineModel();
model.value.options = {
  type: 'text',
  delimiter: ',',
  strip_punctuation: true,
  lowercase: true,
  base_from: false,
};

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
  <section>
    <div>
      <label for="deck-generator__input" class="sr-only"
        >Place your words, separated by commas</label
      >
      <textarea
        name="Words Input"
        id="deck-generator__input"
        class="bg-white dark:text-gray-900 w-full h-40 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2"
        placeholder="Place your words, separated by commas"
        v-model="model.content"
      ></textarea>
    </div>
    <div class="flex flex-col gap-2 p-3">
      <OptionRow
        v-for="(option, key) in options"
        :option="option"
        :key="key"
        v-model="model.options[key]"
      />
    </div>
  </section>
</template>
