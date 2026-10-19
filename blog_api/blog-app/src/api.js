const API = import.meta.env.VITE_API_URL;

export const tokens = {
  get access() { return localStorage.getItem('access'); },
  get refresh() { return localStorage.getItem('refresh'); },
  set({ access, refresh }) {
    if (access) localStorage.setItem('access', access);
    if (refresh) localStorage.setItem('refresh', refresh); // refresh rotates
  },
  clear() {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
  },
};

// One refresh at a time. Rotation blacklists the old refresh token, so two
// parallel refreshes would make the second fail and log the user out.
let refreshing = null;
function refreshAccessToken() {
  refreshing ??= fetch(`${API}/token/refresh/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh: tokens.refresh }),
  })
    .then(async (r) => {
      if (!r.ok) throw new Error('refresh failed');
      tokens.set(await r.json());
    })
    .finally(() => { refreshing = null; });
  return refreshing;
}

export async function apiFetch(path, options = {}) {
  const send = () =>
    fetch(`${API}${path}`, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...(tokens.access && { Authorization: 'Bearer ${tokens.access}' }),
        ...options.headers,
      },
    });

  let res = await send();
  if (res.status === 401 && tokens.refresh) {
    try {
      await refreshAccessToken();
      res = await send();              // retry once with the new token
    } catch {
      tokens.clear();
      window.dispatchEvent(new Event('auth:logout'));
    }
  }
  if (res.status === 429) throw new Error('Too many requests, try again later.');
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `Request failed (${res.status})`);
  }
  return res.status === 204 ? null : res.json();
}