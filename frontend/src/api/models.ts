import type { OptionItem } from '@/types/option';

export async function fetchModels(provider: string): Promise<OptionItem[]> {
  const url = `${import.meta.env.VITE_API_URL}/ai/models/${provider}`;
  const response = await fetch(url, {
    method: 'get',
    credentials: 'include',
  });
  const r = await response.json();
  if (!response.ok) {
    console.log(r);
    throw new Error(
      `Failed to retrieve models for ${provider}. Please verify your API key and try again.`,
    );
  }
  return r;
}
