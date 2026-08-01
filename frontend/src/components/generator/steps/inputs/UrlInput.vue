<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';
import WordSelector from '@/components/ui/WordSelector.vue';
import { extractWordsFromUrl } from '@/api/url';

export interface ExtractedWord {
  text: string
  level: string
}

const generatorStore = useGeneratorStore();
const props = defineProps({
  type: String,
});
const content = defineModel('content');
const placeholder = computed(() => {
  return props.type == 'web' ? 'https://' : 'https://www.youtube.com/watch?v=...';
});
const urlOptionsSchema: Record<string, SchemaField> = {
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
const urlOptions = generatorStore.contentOptions.url;
const selectedWords = ref(['hello', 'yes', 'now']);
const isExtracting = ref(false)
const extractedWords = ref<ExtractedWord[]>([])
async function handleExtract() {
  if (!content.value) return;
  isExtracting.value = true;
  extractedWords.value = await extractWordsFromUrl(
    content.value,
    generatorStore.contentOptions.url,
  );
  isExtracting.value = false;
}
</script>

<template>
  <section>
    <div>
      <input
        type="url"
        :placeholder="placeholder"
        v-model="content"
        class="bg-white dark:text-gray-900 w-full h-10 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2 text-gray-900 placeholder:text-gray-400"
      />
      <div class="flex flex-col gap-4 p-3">
        <OptionRow
          v-for="(option, key) in urlOptionsSchema"
          :option="option"
          :key="key"
          v-model="urlOptions[key as keyof typeof urlOptions]"
        />
      </div>
    </div>
    <button @click="handleExtract" class="bg-primary text-surface p-1 rounded">Extract Words</button>
    <WordSelector :candidates="extractedWords" v-model="selectedWords" />
  </section>
</template>
