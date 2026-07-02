<script setup lang="ts">
import '@/assets/global.css';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';
import FilePicker from '@/components/ui/FilePicker.vue';

const generatorStore = useGeneratorStore();
const content = defineModel<File | null>('content');
const fileOptionsSchema: Record<string, SchemaField> = {
  delimiter: {
    label: 'Delimiter',
    type: 'select',
    items: [
      { label: 'Newline', value: '\n' },
      { label: 'Comma', value: ',' },
      { label: 'Space', value: ' ' },
    ],
  },
  wordColumn: { label: 'Word Column', type: 'range', props: { min: 1, max: 10, step: 1 } },
  hasHeader: { label: 'Has Header', type: 'boolean' },
  stripPunctuation: { label: 'Strip Punctuation', type: 'boolean' },
  lowercase: { label: 'All Lowercase', type: 'boolean' },
  baseForm: { label: 'Base Form Only', type: 'boolean' },
};
const fileOptions = generatorStore.contentOptions.file;
</script>

<template>
  <section>
    <FilePicker :accept="'image/*'" v-model="content" />
    <div class="flex flex-col gap-4 p-3">
      <OptionRow
        v-for="(option, key) in fileOptionsSchema"
        :option="option"
        :key="key"
        v-model="fileOptions[key as keyof typeof fileOptions]"
      />
    </div>
  </section>
</template>
