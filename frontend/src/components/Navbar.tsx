import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Code2 } from 'lucide-react';

export default function Navbar() {
  const { user } = useAuth();

  return (
    <nav className="bg-white border-b border-gray-200 px-6 py-3 flex items-center justify-between flex-shrink-0 z-10">
      <Link to="/" className="flex items-center gap-2">
        <Code2 className="text-blue-600" size={24} />
        <span className="text-lg font-bold text-gray-900">PySolve Academy</span>
      </Link>
      <div className="flex items-center gap-4">
        {!user && (
          <>
            <Link to="/login" className="text-sm text-gray-600 hover:text-gray-900 font-medium">Log in</Link>
            <Link to="/register" className="px-4 py-1.5 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors">
              Get started
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}
