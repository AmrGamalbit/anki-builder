import type { UrlOptions } from '@/types/option';

export async function extractWordsFromUrl(
  url: string,
  urlType: string,
  options: UrlOptions,
): Promise<Record<string, string>> {
  options.type = urlType;
  const payload = { url: url, options: options };
  const response = await fetch(`${import.meta.env.VITE_API_URL}/extract/url`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const r = await response.json();
  if (!response.ok) {
    console.log(r);
    throw new Error('Failed to extract words. Please try again.');
  }
  return r;
}
