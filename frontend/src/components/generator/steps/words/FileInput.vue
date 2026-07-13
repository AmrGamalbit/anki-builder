<script setup lang="ts">
import '@/assets/global.css';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';
import FilePicker from '@/components/ui/FilePicker.vue';
import { ref, watch } from 'vue';
import { extractWordsFromFile } from '@/api/file';
import Modal from '@/components/ui/Modal.vue';

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
    <Modal v-model="showPreview">
      <table class="table-auto w-full text-sm">
        <thead class="bg-gray-50 text-gray-500 uppercase text-sm tracking-wide rounded-2xl">
          <tr>
            <th class="px-4 py-3 text-left font-medium">Index</th>
            <th class="px-4 py-3 text-left font-medium">Word</th>
          </tr>
        </thead>
        <tr
          v-for="(word, index) in generatorStore.content.split(',')"
          class="border-t border-gray-100 even:bg-gray-50 hover:bg-gray-100 transition-colors"
        >
          <td class="px-4 py-3 text-gray-700">{{ index }}</td>
          <td class="px-4 py-3 text-gray-700">{{ word }}</td>
        </tr>
      </table>
    </Modal>
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
