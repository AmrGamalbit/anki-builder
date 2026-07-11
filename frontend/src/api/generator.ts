import { useGeneratorStore } from '@/stores/generator';
import type { CardData } from '@/types/card';

let lastGenerationPayload: string | null = null;

export async function generateDeck() {
  const generatorStore = useGeneratorStore();
  const generationPayload = {
    content: generatorStore.content,
    contentType: generatorStore.contentType,
    contentOptions:
      generatorStore.contentOptions[
        generatorStore.contentType as keyof typeof generatorStore.contentOptions
      ],
    definitionOptions: generatorStore.definitionOptions,
  };
  if (lastGenerationPayload === JSON.stringify(generationPayload)) return;
  generatorStore.isGenerating = true;
  const endpoint =
    generatorStore.definitionOptions.source == 'ai' ? '/ai/generate' : '/dictionary/lookup';
  const payload = {
    ...generationPayload,
    appearance_options: generatorStore.appearanceOptions,
  };
  const res = await fetch(`${import.meta.env.VITE_API_URL}${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
    credentials: 'include',
  });
  const r = await res.json();
  generatorStore.cards = r.data.map((card: CardData) => ({
    id: crypto.randomUUID(),
    term: card.term,
    definition: card.definition,
    synonyms: card.synonyms,
    antonyms: card.antonyms,
    example: card.example,
    partOfSpeech: card.partOfSpeech,
    audioUrl: card.audioUrl,
    pictogramUrl: card.pictogramUrl,
  }));
  generatorStore.pronunciationUrls = r.pronunciations;
  lastGenerationPayload = JSON.stringify(generationPayload);
  generatorStore.isGenerating = false;
}

export async function triggerDownload() {
  const generatorStore = useGeneratorStore();
  if (generatorStore.isGenerating) return;
  generatorStore.isExporting = true;
  const payload = {
    appearanceOptions: generatorStore.appearanceOptions,
    definitionOptions: generatorStore.definitionOptions,
    deckName: generatorStore.deckName,
    pronunciationUrls: generatorStore.pronunciationUrls,
    data: generatorStore.cards.map(({ id, ...rest }) => rest),
  };
  console.log(payload);
  const res = await fetch(`${import.meta.env.VITE_API_URL}/deck/export`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  console.log(res);
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${generatorStore.deckName}.apkg`;
  a.click();
  URL.revokeObjectURL(url);
  generatorStore.isExporting = false;
}
