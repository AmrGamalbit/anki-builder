export async function syncApiKeys() {
  const savedKeys = JSON.parse(localStorage.getItem('apikeys') ?? '{}');
  if (!savedKeys) return;
  const res = await fetch(`${import.meta.env.VITE_API_URL}/auth/apikeys`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(savedKeys),
  });
  const r = await res.json();
  console.log(r);
}
