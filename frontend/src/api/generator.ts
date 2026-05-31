import { useGeneratorStore } from '@/stores/generator';

export async function generateDeck() {
  const generatorStore = useGeneratorStore();
  const endpoint =
    generatorStore.definitionOptions.source == 'ai' ? '/ai/generate' : '/dictionary/lookup';
  const { contentOptions, ...rest } = generatorStore.$state;
  const payload = {
    ...rest,
    contentOptions: contentOptions[generatorStore.contentType as keyof typeof contentOptions],
  };
  console.log(payload);
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const r = await res.json();
    console.log(r);
    return { intent: 'danger', msg: r.detail };
  } else {
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${payload.deckName}.apkg`;
    a.click();
    URL.revokeObjectURL(url);
    return { intent: 'success', msg: 'Deck was generated successfully' };
  }
}
