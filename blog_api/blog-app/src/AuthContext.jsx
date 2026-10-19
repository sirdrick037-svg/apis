import { createContext, useContext, useEffect, useState, useCallback } from 'react';
import { apiFetch, tokens } from './api';

const AuthContext = createContext(null);
export const useAuth = () => useContext(AuthContext);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(!!tokens.access);

  const loadUser = useCallback(async () => {
    try { setUser(await apiFetch('/auth/me/')); }
    catch { setUser(null); }
    finally { setLoading(false); }
  }, []);

  useEffect(() => { if (tokens.access) loadUser(); }, [loadUser]);

  // apiFetch signals when refresh fails
  useEffect(() => {
    const onLogout = () => setUser(null);
    window.addEventListener('auth:logout', onLogout);
    return () => window.removeEventListener('auth:logout', onLogout);
  }, []);

  async function login(email, password) {
    const data = await apiFetch('/token/', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    tokens.set(data);
    await loadUser();
  }

  async function logout() {
    try {
      await apiFetch('/auth/logout/', {
        method: 'POST',
        body: JSON.stringify({ refresh: tokens.refresh }),
      });
    } catch { /* clear locally regardless */ }
    tokens.clear();
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}