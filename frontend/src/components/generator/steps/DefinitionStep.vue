<script setup lang="ts">
import { computed, onMounted, watch } from 'vue';
import LanguagePairSelector from '@/components/generator/deck/LanguagePairSelector.vue';
import type { OptionItem } from '@/types/option';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';
import { ref } from 'vue';
import { fetchModels } from '@/api/models';
import OptionGroup from '@/components/ui/OptionGroup.vue';
import { storeToRefs } from 'pinia';

const availableModels = ref<Record<string, OptionItem[]>>({});
const generatorStore = useGeneratorStore();
const { definitionOptions } = storeToRefs(generatorStore);

type ProviderKey = 'dictionary' | 'ai';
const providers: Record<ProviderKey, OptionItem[]> = {
  dictionary: [
    { label: 'Free Dictionary API', value: 'free_dictionary_api' },
    { label: 'Wordnik', value: 'wordnik' },
  ],
  ai: [
    { label: 'Gemini', value: 'gemini' },
    { label: 'Groq', value: 'groq' },
  ],
};
const isEnglish = computed(() => {
  return (
    definitionOptions.value.targetLanguage == 'en' && definitionOptions.value.sourceLanguage == 'en'
  );
});
const availableSources = computed(() => {
  return isEnglish.value
    ? [
        { label: 'Dictionary', value: 'dictionary' },
        { label: 'AI', value: 'ai' },
      ]
    : [{ label: 'AI', value: 'ai' }];
});
watch(isEnglish, (newIsEnglish) => {
  if (!newIsEnglish) {
    generatorStore.definitionOptions.source = 'ai';
  }
});
async function loadModels() {
  for (const provider of providers.ai) {
    availableModels.value[provider.value] = await fetchModels(provider.value);
  }
}
onMounted(() => loadModels());

const definitionOptionsSchema = computed<Record<string, SchemaField>>(() => {
  return {
    source: {
      label: 'Source',
      type: 'select',
      items: availableSources.value,
    },
    provider: {
      label: 'Provider',
      type: 'select',
      items: providers[generatorStore.definitionOptions.source as ProviderKey],
    },
    mode: {
      label: 'Mode',
      type: 'select',
      items: [
        { label: 'Definition', value: 'definition' },
        { label: 'Translation', value: 'translation' },
      ],
      shouldShow: generatorStore.definitionOptions.source == 'ai',
    },
    model: {
      label: 'Model',
      type: 'choice',
      items: availableModels.value[generatorStore.definitionOptions.provider] ?? [],
      shouldShow: generatorStore.definitionOptions.source == 'ai',
    },
    useDictionaryAudio: {
      label: 'Use Dictionary Audio',
      type: 'boolean',
      shouldShow:
        generatorStore.definitionOptions.cardFields.audio == true &&
        generatorStore.definitionOptions.source == 'dictionary',
    },
  };
});
const cardFieldsSchema: Record<string, SchemaField> = {
  partOfSpeech: { label: 'Part Of Speech', type: 'boolean' },
  example: { label: 'Example', type: 'boolean' },
  synonyms: { label: 'Synonyms', type: 'boolean' },
  antonyms: { label: 'Antonyms', type: 'boolean' },
  audio: { label: 'Audio', type: 'boolean' },
  image: { label: 'Image', type: 'boolean' },
};
const visibleDeckSchema = computed(() =>
  Object.fromEntries(
    Object.entries(definitionOptionsSchema.value).filter(
      ([_, option]) => option?.shouldShow !== false,
    ),
  ),
);
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Definition</h2>
    <hr class="m-5" />
    <div class="flex flex-col gap-5">
      <LanguagePairSelector
        v-model:sourceLanguage="definitionOptions['sourceLanguage']"
        v-model:targetLanguage="definitionOptions['targetLanguage']"
      />
      <OptionGroup
        class="flex flex-col gap-2"
        :schema="visibleDeckSchema"
        v-model="definitionOptions"
      />
      <hr class="border-gray-100" />
      <h4 class="text-sm uppercase tracking-wide text-neutral font-medium">Card Fields</h4>
      <OptionGroup
        class="grid grid-cols-2 gap-4 justify-between"
        :schema="cardFieldsSchema"
        v-model="definitionOptions.cardFields"
      />
    </div>
  </section>
</template>
