import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { DefinitionOptions, AppearanceOptions, ContentOptions } from '@/types/option';
import type { CardData } from '@/types/card';

export const useGeneratorStore = defineStore('generator', () => {
  const content = ref();
  const contentType = ref();
  const duplicatesRemoved = ref();
  const contentOptions = ref<ContentOptions>({
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
      vocabularyLevel: 'b1',
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
    model: '',
    sourceLanguage: 'en',
    targetLanguage: 'en',
    cardFields: {
      partOfSpeech: false,
      example: false,
      synonyms: false,
      antonyms: false,
      audio: false,
      picture: false,
    },
  });
  const appearanceOptions = ref<AppearanceOptions>({
    fontFamily: 'system-ui, sans-serif',
    fontSize: 16,
    lineHeight: 1.4,
    padding: 20,
    textAlign: 'center',
    accentColor: '#6b00c2',
    backgroundColor: '#ffffff',
    color: '#1a1a1a',
    nightMode: true,
  });
  const deckName = ref<string>(
    `${definitionOptions.value.sourceLanguage} - ${definitionOptions.value.targetLanguage}`,
  );
  const cards = ref<CardData[]>([]);
  const pronunciationUrls = ref<string[]>([]);
  const isGenerating = ref<boolean>(false);
  const isExporting = ref<boolean>(false);
  const currentStep = ref<number>(0);

  function processContent() {
    const delimiter = contentOptions.value.text.delimiter;
    const words = content.value.split(delimiter).map((w: string) => w.trim().toLowerCase());
    const uniqueWords = [...new Set(words)];
    content.value = uniqueWords.join(delimiter);
    return words.length - uniqueWords.length;
  }

  function updateCard(index: number, updatedCard: CardData) {
    cards.value[index] = updatedCard;
  }

  function deleteCard(index: number) {
    cards.value.splice(index, 1);
  }

  function addCard() {
    cards.value.push({
      id: crypto.randomUUID(),
      term: '',
      definition: '',
      synonyms: null,
      antonyms: null,
      example: null,
      partOfSpeech: '',
      audioUrl: null,
      pictogramUrl: null,
    });
  }

  return {
    content,
    contentType,
    contentOptions,
    definitionOptions,
    appearanceOptions,
    pronunciationUrls,
    processContent,
    isGenerating,
    isExporting,
    currentStep,
    updateCard,
    deleteCard,
    deckName,
    addCard,
    cards,
  };
});
