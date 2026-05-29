<script setup lang="ts">
import OptionField from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';

const generatorStore = useGeneratorStore();
const content = defineModel<string>('content');
const textOptionsSchema: Record<string, SchemaField> = {
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
const textOptions = generatorStore.contentOptions.text;
</script>

<template>
  <section>
    <div>
      <label for="text-input" class="sr-only">Place your words, separated by commas</label>
      <textarea
        name="Words Input"
        id="text-input"
        class="bg-white dark:text-gray-900 w-full h-40 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2"
        placeholder="Place your words, separated by commas"
        v-model="content"
      ></textarea>
    </div>
    <div class="flex flex-col gap-4 p-3">
      <OptionField
        v-for="(option, key) in textOptionsSchema"
        :option="option"
        :key="key"
        v-model="textOptions[key as keyof typeof textOptions]"
      />
    </div>
  </section>
</template>
