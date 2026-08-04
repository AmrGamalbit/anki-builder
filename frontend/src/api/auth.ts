export async function syncApiKeys() {
  const savedKeys = JSON.parse(localStorage.getItem('apikeys') ?? '{}') as Record<string, string>;
  if (Object.values(savedKeys).every((v) => !v.trim())) return;
  const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/apikeys`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify(savedKeys),
  });
  const r = await response.json();
  if (!response.ok) {
    console.log(r);
    throw new Error('Failed to save API keys. Please try again.');
  }
  return `Successfully saved API keys for: ${r.saved_providers.join(', ')}`;
}
