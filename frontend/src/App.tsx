import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import Landing from './pages/Landing';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import ProblemList from './pages/ProblemList';
import ProblemDetails from './pages/ProblemDetails';
import Compiler from './pages/Compiler';
import Bookmarks from './pages/Bookmarks';

// Authenticated layout with sidebar
function AppLayout({ children }: { children: React.ReactNode }) {
  const { user, loading } = useAuth();
  if (loading) return <div className="flex items-center justify-center h-full text-gray-500">Loading...</div>;
  if (!user) return <Navigate to="/login" replace />;
  return (
    <div className="flex flex-1 overflow-hidden">
      <Sidebar />
      <main className="flex-1 overflow-y-auto bg-gray-50">
        {children}
      </main>
    </div>
  );
}

function AppContent() {
  const { user } = useAuth();
  return (
    <div className="flex flex-col h-screen">
      {!user && <Navbar />}
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<AppLayout><Dashboard /></AppLayout>} />
        <Route path="/problems" element={<AppLayout><ProblemList /></AppLayout>} />
        <Route path="/problem/:id" element={<AppLayout><ProblemDetails /></AppLayout>} />
        <Route path="/compiler" element={<AppLayout><Compiler /></AppLayout>} />
        <Route path="/bookmarks" element={<AppLayout><Bookmarks /></AppLayout>} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </div>
  );
}

export default function App() {
  return (
    <Router basename={import.meta.env.BASE_URL}>
      <AuthProvider>
        <AppContent />
      </AuthProvider>
    </Router>
  );
}

