import type { FileOptions } from '@/types/option';

export async function extractWordsFromFile(
  content: File,
  contentOptions: FileOptions,
): Promise<string> {
  const formData = new FormData();
  formData.append('file', content);
  const entries = Object.entries(contentOptions);
  for (const [key, value] of entries.slice(0, -1)) {
    formData.append(key, String(value));
  }
  const response = await fetch(`${import.meta.env.VITE_API_URL}/extract/file`, {
    method: 'POST',
    body: formData,
  });
  const r = await response.json();
  console.log(r);
  return r;
}
