import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Code2, LayoutDashboard, List, Terminal, Bookmark, LogOut } from 'lucide-react';

const navItems = [
  { to: '/dashboard', icon: LayoutDashboard, label: 'Dashboard' },
  { to: '/problems', icon: List, label: 'Problem List' },
  { to: '/compiler', icon: Terminal, label: 'Python Compiler' },
  { to: '/bookmarks', icon: Bookmark, label: 'Bookmarks' },
];

export default function Sidebar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <aside className="w-60 min-h-full bg-gray-900 text-white flex flex-col flex-shrink-0">
      {/* Logo */}
      <Link to="/" className="flex items-center gap-2 px-5 py-4 border-b border-gray-700">
        <Code2 size={22} className="text-blue-400" />
        <span className="font-bold text-sm text-white">PySolve Academy</span>
      </Link>

      {/* Nav */}
      <nav className="flex-1 px-3 py-4 space-y-1">
        {navItems.map(({ to, icon: Icon, label }) => (
          <Link
            key={to}
            to={to}
            className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-gray-300 hover:bg-gray-800 hover:text-white transition-colors text-sm"
          >
            <Icon size={18} />
            {label}
          </Link>
        ))}
      </nav>

      {/* User footer */}
      {user && (
        <div className="px-3 py-3 border-t border-gray-700">
          <div className="flex items-center gap-3 px-3 py-2 rounded-lg">
            <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0">
              {(user.name?.[0] || user.email?.[0] || 'U').toUpperCase()}
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium text-white truncate">{user.name || user.email}</p>
              <p className="text-xs text-gray-400 truncate">{user.email}</p>
            </div>
          </div>
          <button
            onClick={handleLogout}
            className="mt-2 flex items-center gap-2 w-full px-3 py-2 text-gray-400 hover:text-red-400 hover:bg-gray-800 rounded-lg text-sm transition-colors"
          >
            <LogOut size={16} /> Logout
          </button>
        </div>
      )}
    </aside>
  );
}
