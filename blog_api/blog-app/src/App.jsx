import { useAuth } from './AuthContext';
import Login from './Login';
import BlogList from './BlogList';

function App() {
  const { user, loading, logout } = useAuth();
  if (loading) return <p>Loading…</p>;
  if (!user) return <Login />;                       // simple route guard

  const canWrite = ['admin', 'editor', 'author'].includes(user.role);
  return (
    <main style={{ maxWidth: 720, margin: '0 auto', padding: 16 }}>
      <header style={{ display: 'flex', justifyContent: 'space-between' }}>
        <span>{user.email} ({user.role})</span>
        <button onClick={logout}>Log out</button>
      </header>
      {canWrite && <button>New post</button>}        {/* UI hint only; the API enforces roles */}
      <BlogList />
    </main>
  );
}

export default App;