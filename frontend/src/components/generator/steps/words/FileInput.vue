<script setup lang="ts">
import '@/assets/global.css';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';
import FilePicker from '@/components/ui/FilePicker.vue';
import { ref, watch } from 'vue';
import { extractWordsFromFile } from '@/api/file';

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
const showPreview = ref(false);

watch([content, () => generatorStore.contentOptions.file], async ([newContent, newOptions]) => {
  if (newContent instanceof File) {
    generatorStore.content = await extractWordsFromFile(newContent, newOptions);
  }
});
</script>

<template>
  <section>
    <FilePicker accept=".csv, .xls, .xlsx" v-model="content" />
    <button
      class="flex items-center gap-1.5 text-sm text-primary hover:underline mt-2 cursor-pointer px-5 disabled:text-gray-600"
      @click="showPreview = !showPreview"
      :disabled="!content"
    >
      Preview
    </button>
    <p v-if="showPreview">{{ generatorStore.content }}</p>
    <div class="flex flex-col gap-4 p-3">
      <OptionRow
        v-for="(option, key) in fileOptionsSchema"
        :option="option"
        :key="key"
        v-model="
          generatorStore.contentOptions.file[key as keyof typeof generatorStore.contentOptions.file]
        "
      />
    </div>
  </section>
</template>
