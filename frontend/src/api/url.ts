import type { UrlOptions } from '@/types/option';

export async function extractWordsFromUrl(
  url: string,
  urlType: string,
  options: UrlOptions,
): Promise<string> {
  console.log(urlType)
  options.type = urlType;
  const payload = { url: url, options: options };
  console.log(payload)
  console.log(payload);
  const response = await fetch(`${import.meta.env.VITE_API_URL}/extract/url`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const r = await response.json();
  console.log(r);
  return r;
}
