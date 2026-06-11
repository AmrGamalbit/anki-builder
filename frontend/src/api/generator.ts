import { useGeneratorStore } from '@/stores/generator';

export async function generateDeck() {
  const generatorStore = useGeneratorStore();
  generatorStore.isGenerating = true;
  const endpoint =
    generatorStore.definitionOptions.source == 'ai' ? '/ai/generate' : '/dictionary/lookup';
  const { contentOptions, ...rest } = generatorStore.$state;
  const payload = {
    ...rest,
    contentOptions: contentOptions[generatorStore.contentType as keyof typeof contentOptions],
  };
  const res = await fetch(`${import.meta.env.VITE_API_URL}${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const r = await res.json();
  generatorStore.cards = r.data.map((card) => ({
    id: crypto.randomUUID(),
    front: card.term,
    back: `${card.result}\n${card.example}`,
  }));
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
    data: generatorStore.cards.map((card) => ({
      term: card.front,
      result: card.back.split('\n')[0],
      example: card.back.split('\n')[1],
    })),
  };
  const res = await fetch(`${import.meta.env.VITE_API_URL}/ai/export`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${generatorStore.deckName}.apkg`;
  a.click();
  URL.revokeObjectURL(url);
  generatorStore.isExporting = false;
}
