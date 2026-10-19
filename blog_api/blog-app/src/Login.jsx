import { useState } from 'react';
import { useAuth } from './AuthContext';

export default function Login() {
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);

  async function onSubmit(e) {
    e.preventDefault();
    setBusy(true); setError('');
    try { await login(email, password); }
    catch (err) { setError(err.message); }   // e.g. "No active account found..."
    finally { setBusy(false); }
  }

  return (
    <form onSubmit={onSubmit} style={{ maxWidth: 320, margin: '4rem auto', display: 'grid', gap: 8 }}>
      <h2>Sign in</h2>
      <input type="email" placeholder="Email" value={email}
             onChange={(e) => setEmail(e.target.value)} required />
      <input type="password" placeholder="Password" value={password}
             onChange={(e) => setPassword(e.target.value)} required />
      {error && <p role="alert" style={{ color: 'crimson' }}>{error}</p>}
      <button disabled={busy}>{busy ? 'Signing in…' : 'Sign in'}</button>
    </form>
  );
}