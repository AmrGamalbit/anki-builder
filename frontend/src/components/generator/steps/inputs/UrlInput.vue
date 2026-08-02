<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import WordSelector from '@/components/ui/WordSelector.vue';
import { extractWordsFromUrl } from '@/api/url';
import type { UrlOptions } from '@/types/option';
import { useGeneratorStore } from '@/stores/generator';

export interface ExtractedWord {
  text: string;
  level: string;
}

const props = defineProps({
  urlType: String,
});
const content = defineModel<string>('content');
const options = defineModel<UrlOptions>('options');
const url = ref('');
const placeholder = computed(() => {
  return props.urlType == 'article' ? 'https://' : 'https://www.youtube.com/watch?v=...';
});
const isExtracting = ref(false);
const extractedWords = ref<Record<string, string>>({});
const selectedWords = ref<ExtractedWord[]>([]);
async function handleExtract() {
  if (!url.value) return;
  isExtracting.value = true;
  extractedWords.value = await extractWordsFromUrl(url.value, props.urlType, options.value);
  isExtracting.value = false;
}
watch(selectedWords, (words) => {
  content.value = words.join(', ')
});
const optionsSchema: Record<string, SchemaField> = {
  vocabularyLevel: {
    label: 'Vocabulary Level',
    type: 'select',
    items: [
      { label: 'A1', value: 'a1' },
      { label: 'A2', value: 'a2' },
      { label: 'B1', value: 'b1' },
      { label: 'B2', value: 'b2' },
      { label: 'C1', value: 'c1' },
      { label: 'C2', value: 'C2' },
    ],
  },
  maxCards: {
    label: 'Max Cards',
    type: 'range',
    props: { min: 1, max: 40, step: 1 },
  },
  includeIdioms: {
    label: 'Include idioms',
    type: 'boolean',
  },
};
</script>

<template>
  <section>
    <div>
      <input
        type="url"
        :placeholder="placeholder"
        v-model="url"
        class="bg-white dark:text-gray-900 w-full h-10 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2 text-gray-900 placeholder:text-gray-400"
      />
      <div class="flex flex-col gap-4 p-3">
        <OptionRow
          v-for="(option, key) in optionsSchema"
          :option="option"
          :key="key"
          v-model="options[key as keyof typeof options]"
        />
      </div>
    </div>
    <button @click="handleExtract" class="bg-primary text-surface p-1 rounded">
      Extract Words
    </button>
    <WordSelector :candidates="extractedWords" v-model="selectedWords" />
  </section>
</template>
