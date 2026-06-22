<script setup lang="ts">
import '@/assets/global.css';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';

const generatorStore = useGeneratorStore();
const content = defineModel('content');
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
  <section class="flex flex-col gap-5">
    <div class="w-full py-9 bg-white rounded-sm border border-dashed border-gray-300">
      <div class="flex flex-col items-center gap-4">
        <div class="flex flex-col items-center gap-1">
          <svg
            width="40"
            height="40"
            viewBox="0 0 40 40"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          ></svg>
          <p class="text-gray-400 text-xs">CSV, XLC or XLCX, smaller than 15MB</p>
        </div>

        <div class="flex flex-col items-center gap-2">
          <p class="text-gray-900 text-sm font-medium">Drag and Drop your file here or</p>
          <label class="cursor-pointer">
            <input
              type="file"
              class="hidden"
              @change="
                (e) => {
                  content = (e.target as HTMLInputElement).files?.[0];
                }
              "
            />
            <span
              class="flex w-28 h-9 px-2 bg-primary-muted rounded-full shadow text-white text-xs font-semibold items-center justify-center"
            >
              Choose File
            </span>
          </label>
        </div>
      </div>
    </div>
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
