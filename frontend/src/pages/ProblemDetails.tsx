import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import { AlertCircle, CheckCircle2, ChevronLeft, ChevronRight, X, Bookmark, BookmarkCheck } from 'lucide-react';
import api from '../services/api';

const TOTAL_PROBLEMS = 505;

export default function ProblemDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [problem, setProblem] = useState<any>(null);
  const [code, setCode] = useState('');
  const [inputData, setInputData] = useState('');
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [notice, setNotice] = useState<{ type: 'success' | 'error'; message: string } | null>(null);
  const [isBookmarked, setIsBookmarked] = useState(false);

  useEffect(() => {
    api.get(`/problems/${id}`).then(res => {
      setProblem(res.data);
      setCode(res.data.python_code || '');
      setInputData(res.data.example_input || '');
      setOutput('');
      setNotice(null);
    });
    
    // Check if problem is bookmarked
    api.get(`/bookmarks/check/${id}`).then(res => {
      setIsBookmarked(res.data.bookmarked);
    }).catch(() => {
      setIsBookmarked(false);
    });
  }, [id]);

  useEffect(() => {
    if (!notice) return;

    const timer = window.setTimeout(() => {
      setNotice(null);
    }, 2500);

    return () => window.clearTimeout(timer);
  }, [notice]);

  const handleRun = async () => {
    setIsRunning(true);
    try {
      const res = await api.post('/code/run', { code, input_data: inputData });
      setOutput(res.data.error || res.data.output);
    } catch (err) {
      setOutput('Error executing code');
    }
    setIsRunning(false);
  };

  const handleComplete = async () => {
    try {
      await api.put(`/progress/${id}?status=Completed`);
      setNotice({ type: 'success', message: 'Problem marked as completed' });
    } catch (err) {
      setNotice({ type: 'error', message: 'Could not update progress. Please try again.' });
    }
  };

  const handleBookmark = async () => {
    try {
      if (isBookmarked) {
        await api.delete(`/bookmarks/${id}`);
        setIsBookmarked(false);
        setNotice({ type: 'success', message: 'Bookmark removed' });
      } else {
        await api.post(`/bookmarks/${id}`);
        setIsBookmarked(true);
        setNotice({ type: 'success', message: 'Problem bookmarked' });
      }
    } catch (err) {
      setNotice({ type: 'error', message: 'Could not update bookmark. Please try again.' });
    }
  };

  if (!problem) return <div className="p-8">Loading...</div>;

  const concepts = JSON.parse(problem.concepts || '[]');
  const explanations = JSON.parse(problem.explanation || '[]');
  const dryRun = JSON.parse(problem.dry_run || '{}');
  const problemId = Number(problem.id);
  const hasPrevious = problemId > 1;
  const hasNext = problemId < TOTAL_PROBLEMS;

  const goToProblem = (nextId: number) => {
    navigate(`/problem/${nextId}`);
  };

  return (
    <div className="relative flex h-[calc(100vh-64px)] w-full">
      {notice && (
        <div className="absolute right-6 top-5 z-20 w-[min(360px,calc(100%-48px))] rounded-lg border border-gray-200 bg-white px-4 py-3 shadow-xl">
          <div className="flex items-start gap-3">
            <div className={`mt-0.5 rounded-full p-1 ${notice.type === 'success' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'}`}>
              {notice.type === 'success' ? <CheckCircle2 size={18} /> : <AlertCircle size={18} />}
            </div>
            <div className="min-w-0 flex-1">
              <p className="text-sm font-semibold text-gray-900">
                {notice.type === 'success' ? 'Completed' : 'Update failed'}
              </p>
              <p className="text-sm text-gray-600">{notice.message}</p>
            </div>
            <button
              onClick={() => setNotice(null)}
              className="rounded p-1 text-gray-400 hover:bg-gray-100 hover:text-gray-700"
              aria-label="Close notification"
            >
              <X size={16} />
            </button>
          </div>
        </div>
      )}
      {/* Left side: Problem Description */}
      <div className="w-1/2 p-6 overflow-y-auto border-r bg-white">
        <div className="flex flex-wrap justify-between items-center gap-3 mb-4">
          <h1 className="text-2xl font-bold">{problem.id}. {problem.title}</h1>
          <div className="flex items-center gap-2">
            <button
              onClick={() => goToProblem(problemId - 1)}
              disabled={!hasPrevious}
              className="inline-flex items-center gap-1 px-3 py-1 bg-white border border-gray-300 text-gray-700 rounded hover:bg-gray-50 disabled:opacity-40 disabled:cursor-not-allowed text-sm font-medium"
              title="Previous problem"
            >
              <ChevronLeft size={16} />
              Previous
            </button>
            <button
              onClick={() => goToProblem(problemId + 1)}
              disabled={!hasNext}
              className="inline-flex items-center gap-1 px-3 py-1 bg-white border border-gray-300 text-gray-700 rounded hover:bg-gray-50 disabled:opacity-40 disabled:cursor-not-allowed text-sm font-medium"
              title="Next problem"
            >
              Next
              <ChevronRight size={16} />
            </button>
            <button onClick={handleComplete} className="px-3 py-1 bg-green-100 text-green-700 rounded hover:bg-green-200 text-sm font-medium">Mark Completed</button>
            <button 
              onClick={handleBookmark}
              className={`px-3 py-1 rounded text-sm font-medium flex items-center gap-1 ${
                isBookmarked 
                  ? 'bg-yellow-100 text-yellow-700 hover:bg-yellow-200' 
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              {isBookmarked ? <BookmarkCheck size={16} /> : <Bookmark size={16} />}
              {isBookmarked ? 'Bookmarked' : 'Bookmark'}
            </button>
          </div>
        </div>
        
        <div className="mb-6">
          <h3 className="font-semibold text-lg mb-2 border-b pb-1">Problem Statement</h3>
          <p className="text-gray-700 whitespace-pre-wrap">{problem.description}</p>
        </div>

        {concepts.length > 0 && (
          <div className="mb-6">
            <h3 className="font-semibold text-lg mb-2 border-b pb-1">Concepts</h3>
            <div className="flex gap-2 flex-wrap">
              {concepts.map((c: string, idx: number) => (
                <span key={idx} className="bg-blue-50 text-blue-700 px-2 py-1 rounded text-sm">{c}</span>
              ))}
            </div>
          </div>
        )}

        <div className="mb-6">
          <div className="flex items-center justify-between border-b pb-2 mb-3">
            <h3 className="font-semibold text-lg text-gray-900">Step-by-Step Code Explanation</h3>
            <span className="text-xs bg-indigo-50 text-indigo-700 px-2.5 py-0.5 rounded-full font-medium">Non-IT Friendly</span>
          </div>
          <div className="space-y-3">
            {explanations.map((exp: any, idx: number) => (
              <div key={idx} className="bg-gray-50 border border-gray-200 rounded-lg p-3 hover:border-blue-300 transition-colors">
                <div className="flex items-center gap-2 mb-1.5 flex-wrap">
                  <span className="inline-flex items-center justify-center bg-blue-600 text-white text-xs font-bold px-2 py-0.5 rounded">
                    Step {idx + 1}
                  </span>
                  <code className="text-xs font-mono bg-gray-200 text-gray-800 px-2 py-0.5 rounded">
                    {exp.code}
                  </code>
                </div>
                <p className="text-gray-700 text-sm leading-relaxed pl-1">{exp.explanation}</p>
              </div>
            ))}
          </div>
        </div>

        {((dryRun.columns && dryRun.rows) || (dryRun.steps && dryRun.steps.length > 0)) && (
          <div className="mb-6">
            <div className="flex items-center justify-between border-b pb-2 mb-2">
              <h3 className="font-semibold text-lg text-gray-900">Interactive Dry Run</h3>
              <span className="text-xs text-gray-500 font-mono">Input: {dryRun.input}</span>
            </div>
            <div className="overflow-x-auto rounded-lg border border-gray-200">
              <table className="min-w-full text-sm text-left text-gray-600">
                <thead className="text-xs text-gray-700 uppercase bg-gray-100 border-b">
                  <tr>
                    <th className="px-3 py-2 w-12 text-center">Iter</th>
                    <th className="px-4 py-2">Condition</th>
                    <th className="px-4 py-2">Variables in Memory</th>
                    <th className="px-4 py-2">What Happened</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200 bg-white">
                  {dryRun.steps.map((step: any, idx: number) => (
                    <tr key={idx} className="hover:bg-gray-50">
                      <td className="px-3 py-2 text-center font-bold text-gray-400 text-xs">{step.iteration}</td>
                      <td className="px-4 py-2 font-mono text-xs text-blue-700">
                        {step.condition} {step.result ? `→ ${step.result}` : ''}
                      </td>
                      <td className="px-4 py-2 font-mono text-xs text-purple-700 bg-purple-50/40">
                        {typeof step.variables === 'object' ? JSON.stringify(step.variables) : String(step.variables)}
                      </td>
                      <td className="px-4 py-2 text-xs text-gray-700 leading-relaxed">{step.explanation}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        <div className="grid grid-cols-2 gap-4 mb-6">
          <div className="bg-gray-50 p-3 rounded">
            <span className="font-medium text-sm">Time Complexity:</span> <code className="text-red-600 ml-1">{problem.time_complexity}</code>
          </div>
          <div className="bg-gray-50 p-3 rounded">
            <span className="font-medium text-sm">Space Complexity:</span> <code className="text-red-600 ml-1">{problem.space_complexity}</code>
          </div>
        </div>

      </div>

      {/* Right side: Editor */}
      <div className="w-1/2 flex flex-col h-full bg-gray-900">
        <div className="flex-1">
          <Editor
            height="100%"
            defaultLanguage="python"
            theme="vs-dark"
            value={code}
            onChange={(val) => setCode(val || '')}
            options={{
              minimap: { enabled: false },
              fontSize: 14,
            }}
          />
        </div>
        <div className="h-72 border-t border-gray-700 flex flex-col bg-gray-800 text-white">
          <div className="flex bg-gray-700 p-2 gap-4 items-start">
            <button 
              onClick={handleRun}
              disabled={isRunning}
              className="mt-0.5 px-4 py-1.5 bg-green-600 hover:bg-green-700 rounded text-sm font-medium transition-colors"
            >
              {isRunning ? 'Running...' : 'Run Code'}
            </button>
            <div className="flex-1"></div>
            <label className="mt-2 text-sm text-gray-300">Input:</label>
            <textarea
              className="h-20 w-48 resize-none rounded border border-gray-600 bg-gray-900 px-2 py-1 font-mono text-sm text-white focus:outline-none focus:ring-1 focus:ring-blue-500"
              value={inputData}
              onChange={(e) => setInputData(e.target.value)}
              placeholder={'2\n3'}
            />
          </div>
          <div className="flex-1 p-3 font-mono text-sm overflow-y-auto whitespace-pre-wrap">
            {output || <span className="text-gray-500 italic">Output will appear here...</span>}
          </div>
        </div>
      </div>
    </div>
  );
}
