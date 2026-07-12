<script setup lang="ts">
import { computed, onMounted } from 'vue';
import OptionField from '@/components/ui/OptionField.vue';
import LanguagePairSelector from '@/components/generator/deck/LanguagePairSelector.vue';
import type { OptionItem } from '@/types/option';
import type { SchemaField } from '@/types/schema';
import { useGeneratorStore } from '@/stores/generator';
import { ref, watch } from 'vue';
import { fetchModels } from '@/api/models';

const generatorStore = useGeneratorStore();
const availableModels = ref<Record<string, OptionItem[]>>({});

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

async function loadModels() {
  for (const provider of providers.ai) {
    availableModels.value[provider.value] = await fetchModels(provider.value);
  }
}
onMounted(() => loadModels());

const definitionOptionsSchema = computed<Record<string, SchemaField>>(() => {
  return {
    includePronunciation: {
      label: 'Include Pronunciation',
      type: 'boolean',
    },
    includePictogram: {
      label: 'Include Pictograms',
      type: 'boolean',
    },
    source: {
      label: 'Source',
      type: 'select',
      items: [
        { label: 'Dictionary', value: 'dictionary' },
        { label: 'AI', value: 'ai' },
      ],
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
        generatorStore.definitionOptions.includePronunciation == true &&
        generatorStore.definitionOptions.source == 'dictionary',
    },
  };
});
const definitionOptions = generatorStore.definitionOptions;
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
      <div class="flex flex-col gap-4">
        <OptionField
          v-for="(option, key) in visibleDeckSchema"
          :key="key"
          :option="option"
          v-model="definitionOptions[key as keyof typeof definitionOptions]"
        />
      </div>
    </div>
  </section>
</template>
