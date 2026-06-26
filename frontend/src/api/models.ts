import type { OptionItem } from '@/types/option';

export async function fetchModels(provider: string): Promise<OptionItem[]> {
  const url = `${import.meta.env.VITE_API_URL}/ai/models/${provider}`;
  const res = await fetch(url, {
    method: 'get',
  });
  const r = await res.json();
  return r;
}
