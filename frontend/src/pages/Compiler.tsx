import { useState, useRef } from 'react';
import Editor from '@monaco-editor/react';
import api from '../services/api';
import { Play, RotateCcw, Trash2, Copy, Clock } from 'lucide-react';

const DEFAULT_CODE = `# Welcome to PySolve Academy Python Compiler
# Write your Python code here and press Run!

n = int(input("Enter a number: "))

if n % 2 == 0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")
`;

export default function Compiler() {
  const [code, setCode] = useState(DEFAULT_CODE);
  const [inputData, setInputData] = useState('10');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');
  const [execTime, setExecTime] = useState<number | null>(null);
  const [isRunning, setIsRunning] = useState(false);
  const editorRef = useRef<any>(null);

  const handleRun = async () => {
    setIsRunning(true);
    setOutput('');
    setError('');
    setExecTime(null);
    try {
      const res = await api.post('/code/run', { code, input_data: inputData });
      setOutput(res.data.output || '');
      setError(res.data.error || '');
      setExecTime(res.data.execution_time);
    } catch (err) {
      setError('Failed to connect to execution server.');
    }
    setIsRunning(false);
  };

  const handleKeyDown = (e: KeyboardEvent) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      handleRun();
    }
  };

  const handleReset = () => {
    setCode(DEFAULT_CODE);
    setOutput('');
    setError('');
    setExecTime(null);
  };

  const handleClear = () => {
    setCode('');
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-64px)] bg-gray-900">
      {/* Toolbar */}
      <div className="flex items-center gap-2 px-4 py-2 bg-gray-800 border-b border-gray-700">
        <span className="text-gray-300 font-semibold text-sm">Python Compiler</span>
        <div className="h-4 w-px bg-gray-600 mx-2" />
        <button
          onClick={handleRun}
          disabled={isRunning}
          className="flex items-center gap-1.5 px-4 py-1.5 bg-green-600 hover:bg-green-500 text-white rounded text-sm font-medium transition-colors disabled:opacity-50"
        >
          <Play size={14} />
          {isRunning ? 'Running...' : 'Run'}
          <kbd className="ml-1 text-xs text-green-200 border border-green-500 rounded px-1">Ctrl+Enter</kbd>
        </button>
        <button onClick={handleReset} className="flex items-center gap-1.5 px-3 py-1.5 bg-gray-700 hover:bg-gray-600 text-gray-200 rounded text-sm transition-colors">
          <RotateCcw size={14} /> Reset
        </button>
        <button onClick={handleClear} className="flex items-center gap-1.5 px-3 py-1.5 bg-gray-700 hover:bg-gray-600 text-gray-200 rounded text-sm transition-colors">
          <Trash2 size={14} /> Clear
        </button>
        <button onClick={handleCopy} className="flex items-center gap-1.5 px-3 py-1.5 bg-gray-700 hover:bg-gray-600 text-gray-200 rounded text-sm transition-colors">
          <Copy size={14} /> Copy
        </button>
        {execTime !== null && (
          <span className="ml-auto flex items-center gap-1 text-gray-400 text-xs">
            <Clock size={12} /> {(execTime * 1000).toFixed(1)} ms
          </span>
        )}
      </div>

      {/* Editor + I/O */}
      <div className="flex flex-1 overflow-hidden">
        {/* Monaco Editor */}
        <div className="flex-1 overflow-hidden" onKeyDown={handleKeyDown as any}>
          <Editor
            height="100%"
            defaultLanguage="python"
            theme="vs-dark"
            value={code}
            onChange={(val) => setCode(val || '')}
            onMount={(editor) => { editorRef.current = editor; }}
            options={{
              minimap: { enabled: false },
              fontSize: 15,
              fontFamily: 'Fira Code, Cascadia Code, Consolas, monospace',
              fontLigatures: true,
              lineNumbers: 'on',
              scrollBeyondLastLine: false,
              padding: { top: 12, bottom: 12 },
              automaticLayout: true,
            }}
          />
        </div>

        {/* I/O Panel */}
        <div className="w-96 flex flex-col border-l border-gray-700">
          {/* Input */}
          <div className="flex flex-col h-1/3 border-b border-gray-700">
            <div className="px-3 py-2 bg-gray-800 text-xs font-semibold text-gray-400 uppercase tracking-wide">
              Input (stdin)
            </div>
            <textarea
              className="flex-1 bg-gray-900 text-gray-100 font-mono text-sm p-3 resize-none focus:outline-none focus:ring-1 focus:ring-blue-500"
              value={inputData}
              onChange={e => setInputData(e.target.value)}
              placeholder="Enter program input here..."
            />
          </div>

          {/* Output */}
          <div className="flex flex-col flex-1">
            <div className="px-3 py-2 bg-gray-800 text-xs font-semibold text-gray-400 uppercase tracking-wide flex items-center justify-between">
              <span>Output</span>
              {error ? (
                <span className="text-red-400 text-xs">⚠ Error</span>
              ) : output ? (
                <span className="text-green-400 text-xs">✓ Success</span>
              ) : null}
            </div>
            <div className="flex-1 p-3 font-mono text-sm overflow-y-auto bg-gray-900">
              {error ? (
                <pre className="text-red-400 whitespace-pre-wrap">{error}</pre>
              ) : output ? (
                <pre className="text-green-300 whitespace-pre-wrap">{output}</pre>
              ) : (
                <span className="text-gray-600 italic">Output appears here after running...</span>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
