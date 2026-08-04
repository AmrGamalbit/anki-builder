<script setup lang="ts">
import '@/assets/global.css';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import FilePicker from '@/components/ui/FilePicker.vue';
import { ref, watch } from 'vue';
import { extractWordsFromFile } from '@/api/file';
import Modal from '@/components/ui/Modal.vue';
import type { FileOptions } from '@/types/option';
import Alert from '@/components/ui/Alert.vue';

const content = defineModel<File | null>('content');
const options = defineModel<FileOptions>('options');
const error = ref<string | null>('');
const showPreview = ref(false);
const optionsSchema: Record<string, SchemaField> = {
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

watch([content, options], async ([newContent, newOptions]) => {
  if (newContent instanceof File) {
    try {
      content.value = await extractWordsFromFile(newContent, newOptions);
    } catch (e: any) {
      error.value = e.message;
    }
  }
});
</script>

<template>
  <section>
    <FilePicker accept=".csv, .xls, .xlsx" v-model="content" />
    <button
      class="flex items-center gap-1.5 text-sm text-primary transition-all duration-200 hover:brightness-140 hover:scale-[1.05] hover:tracking-wider font-semibold mt-2 cursor-pointer px-5 disabled:text-disabled"
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
          v-for="(word, index) in content.split(',')"
          class="border-t border-gray-100 even:bg-gray-50 hover:bg-gray-100 transition-colors"
        >
          <td class="px-4 py-3 text-gray-700">{{ index }}</td>
          <td class="px-4 py-3 text-gray-700">{{ word }}</td>
        </tr>
      </table>
    </Modal>
    <div class="flex flex-col gap-4 p-3">
      <OptionRow
        v-for="(option, key) in optionsSchema"
        :option="option"
        :key="key"
        v-model="options[key as keyof typeof options]"
      />
    </div>
    <Alert v-if="error" intent="danger" :title="error" @close="error = null" />
  </section>
</template>
