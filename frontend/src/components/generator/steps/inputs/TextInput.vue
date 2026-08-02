<script setup lang="ts">
import OptionField from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import type { TextOptions } from '@/types/option';

const content = defineModel<string>('content');
const options = defineModel<TextOptions>('options')
const optionsSchema: Record<string, SchemaField> = {
  delimiter: {
    label: 'Delimiter',
    type: 'select' as const,
    items: [
      { label: 'Newline', value: '\n' },
      { label: 'Comma', value: ',' },
      { label: 'Space', value: ' ' },
    ],
  },
  stripPunctuation: { label: 'Strip Punctuation', type: 'boolean' },
  lowercase: { label: 'All Lowercase', type: 'boolean' },
  baseForm: { label: 'Base Form Only', type: 'boolean' },
};
</script>

<template>
  <section>
    <div>
      <label for="text-input" class="sr-only">Place your words, separated by commas</label>
      <textarea
        name="Words Input"
        id="text-input"
        class="bg-white dark:text-gray-900 w-full h-40 rounded-b-sm border border-gray-300 border-dashed focus:outline-none p-2"
        placeholder="Place your words, separated by commas"
        v-model="content"
      ></textarea>
    </div>
    <div class="flex flex-col gap-4 p-3">
      <OptionField
        v-for="(option, key) in optionsSchema"
        :option="option"
        :key="key"
        v-model="options[key as keyof typeof options]"
      />
    </div>
  </section>
</template>
