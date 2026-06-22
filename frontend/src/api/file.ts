import { useGeneratorStore } from '@/stores/generator';

const generatorStore = useGeneratorStore();
export async function extractWordsFromFile() {
  const formData = new FormData();
  formData.append('file', generatorStore.content);
  const entries = Object.entries(generatorStore.contentOptions.file);
  for (const [key, value] of entries.slice(0, -1)) {
    formData.append(key, String(value));
  }
  const response = await fetch(`${import.meta.env.VITE_API_URL}/file/extract`, {
    method: 'POST',
    body: formData,
  });
  const r = await response.json();
  generatorStore.content = r;
}
