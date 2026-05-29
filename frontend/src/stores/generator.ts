import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import type { DefinitionOptions, AppearanceOptions } from '@/types/option';

export const useGeneratorStore = defineStore('generator', () => {
  const content = ref();
  const contentType = ref();
  const contentOptions = ref({
    file: {
      type: 'file',
      delimiter: ',',
      wordColumn: 1,
      hasHeader: false,
      stripPunctuation: true,
      lowercase: true,
      baseForm: false,
    },
    text: {
      type: 'text',
      delimiter: ',',
      stripPunctuation: true,
      lowercase: true,
      baseForm: false,
    },
    url: {
      vocabulary_level: 'b1',
      maxCards: 20,
      includeIdioms: true,
    },
  });
  const definitionOptions = ref<DefinitionOptions>({
    includePronunciation: false,
    includePictogram: false,
    useDictionaryAudio: false,
    source: 'dictionary',
    provider: 'free_dictionary_api',
    mode: 'definition',
    sourceLanguage: 'en',
    targetLanguage: 'en',
  });
  const appearanceOptions = ref<AppearanceOptions>({
    fontFamily: 'system-ui, sans-serif',
    fontSize: 16,
    lineHeight: 1.4,
    padding: 20,
    textAlign: 'center',
    accentColor: 'blue',
    backgroundColor: '#ffffff',
    color: '#1a1a1a',
    nightMode: true,
  });
  const deckName = ref(
    `${definitionOptions.value.sourceLanguage} - ${definitionOptions.value.targetLanguage}`,
  );

  return { content, contentType, contentOptions, definitionOptions, appearanceOptions, deckName };
});
