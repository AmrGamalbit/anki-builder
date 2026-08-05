<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import { watchDebounced } from '@vueuse/core';
import OptionRow from '@/components/ui/OptionField.vue';
import type { SchemaField } from '@/types/schema';
import { extractWordsFromUrl } from '@/api/url';
import type { UrlOptions } from '@/types/option';
import TermSelector from '@/components/ui/TermSelector.vue';
import Alert from '@/components/ui/Alert.vue';

export interface ExtractedWord {
  text: string;
  level: string;
}

const props = defineProps({
  urlType: String,
});
const content = defineModel<string>('content', { default: '' });
const options = defineModel<UrlOptions>('options', { default: () => {} });
const url = ref('');
const placeholder = computed(() => {
  return props.urlType == 'article' ? 'https://' : 'https://www.youtube.com/watch?v=...';
});
const error = ref<string | null>('');
const isExtracting = ref(false);
const terms = ref<Record<string, string>>({});
const selectedTerms = ref<string[]>([]);
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
  // maxCards: {
  //   label: 'Max Cards',
  //   type: 'range',
  //   props: { min: 1, max: 40, step: 1 },
  // },
  // includeIdioms: {
  //   label: 'Include idioms',
  //   type: 'boolean',
  // },
};

watch(selectedTerms, (words) => {
  content.value = words.join(', ');
});

watchDebounced(
  url,
  async (newUrl) => {
    if (!newUrl || !props.urlType) return;
    isExtracting.value = true;
    try {
      terms.value = await extractWordsFromUrl(url.value, props.urlType, options.value);
    } catch (e: any) {
      console.log('error detected');
      error.value = e.message;
    }
    isExtracting.value = false;
  },
  { debounce: 1000 },
);

const filteredTerms = computed(() => {
  const targetLevel = options.value.vocabularyLevel;
  return Object.fromEntries(
    Object.entries(terms.value).filter(([_, level]) => level.toLowerCase() == targetLevel),
  );
});
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
    <TermSelector v-model:terms="filteredTerms" v-model:selected="selectedTerms" :loading="isExtracting" />
    <Alert v-if="error" intent="danger" :title="error" @close="error = null" />
  </section>
</template>
