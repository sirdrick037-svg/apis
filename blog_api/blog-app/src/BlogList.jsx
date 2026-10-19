import { useEffect, useState } from 'react';
import { apiFetch } from './api';

export default function BlogList() {
  const [data, setData] = useState({ results: [], count: 0 });
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState('');
  const [query, setQuery] = useState('');       // debounced search
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const t = setTimeout(() => { setQuery(search); setPage(1); }, 400);
    return () => clearTimeout(t);
  }, [search]);

  useEffect(() => {
    const controller = new AbortController();
    setLoading(true); setError('');
    const params = new URLSearchParams({ page, ordering: '-published_date' });
    if (query) params.set('search', query);

    apiFetch(`/v1/blogs/?${params}`, { signal: controller.signal })
      .then(setData)
      .catch((e) => { if (e.name !== 'AbortError') setError(e.message); })
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [page, query]);

  const pageSize = 10;                           // matches PAGE_SIZE in settings
  const pages = Math.max(1, Math.ceil(data.count / pageSize));

  return (
    <section>
      <input placeholder="Search blogs…" value={search}
             onChange={(e) => setSearch(e.target.value)} />
      {error && <p role="alert" style={{ color: 'crimson' }}>{error}</p>}
      {loading && <p>Loading…</p>}

      <ul style={{ listStyle: 'none', padding: 0, display: 'grid', gap: 16 }}>
        {data.results.map((b) => (
          <li key={b.id} style={{ border: '1px solid #ddd', borderRadius: 8, overflow: 'hidden' }}>
            {b.image && (
              <img src={b.image} alt="" style={{ width: '100%', height: 180, objectFit: 'cover' }} />
            )}
            <div style={{ padding: 12 }}>
              <h3>{b.title}</h3>
              <small>{b.author_name} · {new Date(b.published_date).toLocaleDateString()}</small>
              <p>{b.text.length > 160 ? b.text.slice(0, 160) + '…' : b.text}</p>
            </div>
          </li>
        ))}
      </ul>

      <button disabled={!data.previous || loading} onClick={() => setPage((p) => p - 1)}>Prev</button>
      <span> Page {page} of {pages} </span>
      <button disabled={!data.next || loading} onClick={() => setPage((p) => p + 1)}>Next</button>
    </section>
  );
}