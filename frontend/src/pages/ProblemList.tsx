import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import { Search, ChevronRight } from 'lucide-react';

const difficultyColor: Record<string, string> = {
  Easy: 'bg-green-100 text-green-800',
  Medium: 'bg-yellow-100 text-yellow-800',
  Hard: 'bg-red-100 text-red-800',
};

export default function ProblemList() {
  const [problems, setProblems] = useState<any[]>([]);
  const [filtered, setFiltered] = useState<any[]>([]);
  const [search, setSearch] = useState('');
  const [difficulty, setDifficulty] = useState('All');
  const [page, setPage] = useState(0);
  const pageSize = 50;

  useEffect(() => {
    api.get('/problems?skip=0&limit=505')
      .then(res => {
        if (Array.isArray(res.data)) {
          setProblems(res.data);
          setFiltered(res.data);
        }
      })
      .catch(() => {});
  }, []);

  useEffect(() => {
    let f = problems;
    if (search) f = f.filter(p => p.title.toLowerCase().includes(search.toLowerCase()));
    if (difficulty !== 'All') f = f.filter(p => p.difficulty === difficulty);
    setFiltered(f);
    setPage(0);
  }, [search, difficulty, problems]);

  const paginated = filtered.slice(page * pageSize, (page + 1) * pageSize);

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Problem List</h1>
          <p className="text-gray-500 text-sm mt-1">{filtered.length} problems</p>
        </div>
      </div>

      {/* Filters */}
      <div className="flex gap-3 mb-6">
        <div className="relative flex-1 max-w-xs">
          <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
          <input
            type="text"
            placeholder="Search problems..."
            value={search}
            onChange={e => setSearch(e.target.value)}
            className="pl-9 pr-3 py-2 border border-gray-300 rounded-lg w-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <select
          value={difficulty}
          onChange={e => setDifficulty(e.target.value)}
          className="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="All">All Difficulties</option>
          <option value="Easy">Easy</option>
          <option value="Medium">Medium</option>
          <option value="Hard">Hard</option>
        </select>
      </div>

      {/* Table */}
      <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">#</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Title</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Phase</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Difficulty</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase"></th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-100">
            {paginated.map((problem) => (
              <tr key={problem.id} className="hover:bg-blue-50 transition-colors">
                <td className="px-6 py-3 text-sm text-gray-400">{problem.id}</td>
                <td className="px-6 py-3 text-sm font-medium text-gray-900">{problem.title}</td>
                <td className="px-6 py-3 text-sm text-gray-500">Phase {problem.phase}</td>
                <td className="px-6 py-3">
                  <span className={`px-2 py-0.5 inline-flex text-xs leading-5 font-semibold rounded-full ${difficultyColor[problem.difficulty] || 'bg-gray-100 text-gray-600'}`}>
                    {problem.difficulty}
                  </span>
                </td>
                <td className="px-6 py-3 text-right">
                  <Link to={`/problem/${problem.id}`} className="flex items-center justify-end gap-1 text-blue-600 hover:text-blue-800 text-sm font-medium">
                    Solve <ChevronRight size={16} />
                  </Link>
                </td>
              </tr>
            ))}
            {paginated.length === 0 && (
              <tr><td colSpan={5} className="px-6 py-8 text-center text-gray-400">No problems found</td></tr>
            )}
          </tbody>
        </table>
        <div className="px-6 py-3 bg-gray-50 border-t border-gray-200 flex items-center justify-between">
          <p className="text-sm text-gray-500">Showing {page * pageSize + 1}–{Math.min((page + 1) * pageSize, filtered.length)} of {filtered.length}</p>
          <div className="flex gap-2">
            <button onClick={() => setPage(p => Math.max(0, p - 1))} disabled={page === 0} className="px-3 py-1 text-sm border border-gray-300 rounded disabled:opacity-40 hover:bg-gray-100">Prev</button>
            <button onClick={() => setPage(p => p + 1)} disabled={(page + 1) * pageSize >= filtered.length} className="px-3 py-1 text-sm border border-gray-300 rounded disabled:opacity-40 hover:bg-gray-100">Next</button>
          </div>
        </div>
      </div>
    </div>
  );
}
