import { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';
import { Link } from 'react-router-dom';
import { CheckCircle2, BookOpen, TrendingUp, ArrowRight } from 'lucide-react';

export default function Dashboard() {
  const { user } = useAuth();
  const [progress, setProgress] = useState<any[]>([]);

  useEffect(() => {
    api.get('/progress')
      .then(res => setProgress(res.data))
      .catch(() => {});
  }, []);

  const completed = progress.filter(p => p.status === 'Completed').length;
  const inProgress = progress.filter(p => p.status === 'In Progress').length;
  const total = 505;

  return (
    <div className="p-8 max-w-5xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Welcome back, {user?.name}! 👋</h1>
        <p className="text-gray-500 mt-1">Keep going — every problem you solve brings you closer to mastery.</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
          <p className="text-xs text-gray-500 uppercase font-medium mb-1">Total Problems</p>
          <p className="text-3xl font-bold text-gray-900">{total}</p>
        </div>
        <div className="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
          <p className="text-xs text-gray-500 uppercase font-medium mb-1">Completed</p>
          <p className="text-3xl font-bold text-green-600">{completed}</p>
        </div>
        <div className="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
          <p className="text-xs text-gray-500 uppercase font-medium mb-1">In Progress</p>
          <p className="text-3xl font-bold text-yellow-600">{inProgress}</p>
        </div>
        <div className="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
          <p className="text-xs text-gray-500 uppercase font-medium mb-1">Remaining</p>
          <p className="text-3xl font-bold text-gray-700">{total - completed}</p>
        </div>
      </div>

      {/* Progress bar */}
      <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm mb-6">
        <div className="flex justify-between items-center mb-3">
          <h2 className="font-semibold text-gray-900">Overall Progress</h2>
          <span className="text-sm text-gray-500">{completed} / {total}</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-3">
          <div
            className="bg-blue-600 h-3 rounded-full transition-all duration-500"
            style={{ width: `${(completed / total) * 100}%` }}
          />
        </div>
        <p className="text-xs text-gray-400 mt-2">{((completed / total) * 100).toFixed(1)}% complete</p>
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Link to="/problems" className="bg-blue-600 text-white p-5 rounded-xl hover:bg-blue-700 transition-colors flex items-center justify-between">
          <div>
            <BookOpen size={24} className="mb-2" />
            <p className="font-semibold">Browse Problems</p>
            <p className="text-blue-200 text-sm mt-1">Start from Phase 1</p>
          </div>
          <ArrowRight size={20} className="text-blue-300" />
        </Link>
        <Link to="/compiler" className="bg-gray-900 text-white p-5 rounded-xl hover:bg-gray-800 transition-colors flex items-center justify-between">
          <div>
            <TrendingUp size={24} className="mb-2" />
            <p className="font-semibold">Python Compiler</p>
            <p className="text-gray-400 text-sm mt-1">Write & run code</p>
          </div>
          <ArrowRight size={20} className="text-gray-500" />
        </Link>
        <Link to="/problem/1" className="bg-green-600 text-white p-5 rounded-xl hover:bg-green-700 transition-colors flex items-center justify-between">
          <div>
            <CheckCircle2 size={24} className="mb-2" />
            <p className="font-semibold">Continue Learning</p>
            <p className="text-green-200 text-sm mt-1">Problem 1: Even or Odd</p>
          </div>
          <ArrowRight size={20} className="text-green-300" />
        </Link>
      </div>
    </div>
  );
}
