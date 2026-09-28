import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Bookmark, Trash2, BookOpen } from 'lucide-react';
import api from '../services/api';

interface BookmarkProblem {
  id: number;
  problem_id: number;
  problem_title: string;
  problem_difficulty: string;
  problem_phase: number;
  created_at: string;
}

export default function Bookmarks() {
  const navigate = useNavigate();
  const [bookmarks, setBookmarks] = useState<BookmarkProblem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchBookmarks();
  }, []);

  const fetchBookmarks = async () => {
    try {
      const res = await api.get('/bookmarks');
      setBookmarks(Array.isArray(res.data) ? res.data : []);
      setLoading(false);
    } catch (err) {
      setError('Failed to load bookmarks');
      setLoading(false);
    }
  };

  const handleRemoveBookmark = async (problemId: number) => {
    try {
      await api.delete(`/bookmarks/${problemId}`);
      setBookmarks(bookmarks.filter(b => b.problem_id !== problemId));
    } catch (err) {
      setError('Failed to remove bookmark');
    }
  };

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty.toLowerCase()) {
      case 'easy':
        return 'bg-green-100 text-green-700';
      case 'medium':
        return 'bg-yellow-100 text-yellow-700';
      case 'hard':
        return 'bg-red-100 text-red-700';
      default:
        return 'bg-gray-100 text-gray-700';
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="text-gray-500">Loading bookmarks...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="flex items-center gap-3 mb-8">
          <Bookmark size={32} className="text-blue-600" />
          <h1 className="text-3xl font-bold text-gray-900">My Bookmarks</h1>
        </div>

        {error && (
          <div className="mb-4 p-4 bg-red-50 border border-red-200 text-red-700 rounded-lg">
            {error}
          </div>
        )}

        {bookmarks.length === 0 ? (
          <div className="text-center py-16 bg-white rounded-lg shadow-sm">
            <Bookmark size={64} className="mx-auto text-gray-300 mb-4" />
            <h2 className="text-xl font-semibold text-gray-700 mb-2">No bookmarks yet</h2>
            <p className="text-gray-500 mb-6">Start bookmarking problems to build your collection</p>
            <button
              onClick={() => navigate('/problems')}
              className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
            >
              Browse Problems
            </button>
          </div>
        ) : (
          <div className="grid gap-4">
            {bookmarks.map((bookmark) => (
              <div
                key={bookmark.id}
                className="bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow p-6 border border-gray-200"
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="text-sm font-mono text-gray-500">#{bookmark.problem_id}</span>
                      <span className={`px-2 py-0.5 rounded text-xs font-medium ${getDifficultyColor(bookmark.problem_difficulty)}`}>
                        {bookmark.problem_difficulty}
                      </span>
                      <span className="text-xs text-gray-400">
                        Phase {bookmark.problem_phase}
                      </span>
                    </div>
                    <h3 className="text-lg font-semibold text-gray-900 mb-2">{bookmark.problem_title}</h3>
                    <p className="text-sm text-gray-500">
                      Bookmarked on {new Date(bookmark.created_at).toLocaleDateString()}
                    </p>
                  </div>
                  <div className="flex items-center gap-2 ml-4">
                    <button
                      onClick={() => navigate(`/problem/${bookmark.problem_id}`)}
                      className="flex items-center gap-1 px-3 py-1.5 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors text-sm"
                    >
                      <BookOpen size={16} />
                      Solve
                    </button>
                    <button
                      onClick={() => handleRemoveBookmark(bookmark.problem_id)}
                      className="p-1.5 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded transition-colors"
                      title="Remove bookmark"
                    >
                      <Trash2 size={18} />
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
