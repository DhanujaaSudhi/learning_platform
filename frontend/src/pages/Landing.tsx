import { Link } from 'react-router-dom';
import { Code2, Terminal, Zap, BookOpen, TrendingUp, Award } from 'lucide-react';

const phases = [
  { num: 1, name: 'Python Logic & Basics', count: 30, color: 'bg-blue-100 text-blue-800 border-blue-200' },
  { num: 2, name: 'Strings', count: 25, color: 'bg-green-100 text-green-800 border-green-200' },
  { num: 3, name: 'Arrays / Lists', count: 35, color: 'bg-yellow-100 text-yellow-800 border-yellow-200' },
  { num: 4, name: 'Searching & Sorting', count: 25, color: 'bg-orange-100 text-orange-800 border-orange-200' },
  { num: 5, name: 'Hashing / Sets', count: 20, color: 'bg-purple-100 text-purple-800 border-purple-200' },
  { num: 6, name: 'Two Pointers & Sliding Window', count: 25, color: 'bg-pink-100 text-pink-800 border-pink-200' },
  { num: 7, name: 'Stack & Queue', count: 20, color: 'bg-red-100 text-red-800 border-red-200' },
  { num: 8, name: 'Linked List', count: 25, color: 'bg-indigo-100 text-indigo-800 border-indigo-200' },
  { num: 9, name: 'Recursion & Backtracking', count: 25, color: 'bg-teal-100 text-teal-800 border-teal-200' },
  { num: 10, name: 'Trees & BST', count: 30, color: 'bg-cyan-100 text-cyan-800 border-cyan-200' },
  { num: 11, name: 'Graphs', count: 25, color: 'bg-lime-100 text-lime-800 border-lime-200' },
  { num: 12, name: 'Dynamic Programming', count: 20, color: 'bg-emerald-100 text-emerald-800 border-emerald-200' },
  { num: 13, name: 'Advanced Arrays', count: 20, color: 'bg-violet-100 text-violet-800 border-violet-200' },
  { num: 14, name: 'Advanced Strings', count: 20, color: 'bg-rose-100 text-rose-800 border-rose-200' },
  { num: 15, name: 'Advanced Hashing', count: 20, color: 'bg-sky-100 text-sky-800 border-sky-200' },
  { num: 16, name: 'Advanced Stack & Queue', count: 20, color: 'bg-amber-100 text-amber-800 border-amber-200' },
  { num: 17, name: 'Advanced Linked List', count: 20, color: 'bg-fuchsia-100 text-fuchsia-800 border-fuchsia-200' },
  { num: 18, name: 'Advanced Trees', count: 25, color: 'bg-green-100 text-green-800 border-green-200' },
  { num: 19, name: 'Advanced Graphs', count: 25, color: 'bg-blue-100 text-blue-800 border-blue-200' },
  { num: 20, name: 'Advanced Graphs / MST', count: 15, color: 'bg-red-100 text-red-800 border-red-200' },
  { num: 21, name: 'Advanced DP', count: 25, color: 'bg-purple-100 text-purple-800 border-purple-200' },
  { num: 22, name: 'Hard DP / Interview Problems', count: 10, color: 'bg-gray-100 text-gray-800 border-gray-200' },
];

const features = [
  { icon: BookOpen, title: 'Step-by-Step Explanations', desc: 'Every line of code explained in plain English.' },
  { icon: Terminal, title: 'Live Python Compiler', desc: 'Run your code directly in the browser.' },
  { icon: Zap, title: 'Interactive Dry Runs', desc: 'Trace loops and variables iteration by iteration.' },
  { icon: TrendingUp, title: 'Progress Tracking', desc: 'Know exactly where you are in your journey.' },
  { icon: Award, title: 'Interview Prep', desc: '505 problems from easy to hard, interview-ready.' },
  { icon: Code2, title: 'Beginner Friendly', desc: 'Designed for MCA/BSc CS students and beginners.' },
];

export default function Landing() {
  return (
    <div className="min-h-screen bg-white">
      {/* Hero */}
      <section className="bg-gradient-to-br from-blue-600 to-indigo-700 text-white py-20 px-6">
        <div className="max-w-5xl mx-auto text-center">
          <h1 className="text-5xl font-bold mb-4 leading-tight">Master Python Problem Solving</h1>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Learn Python from basics to advanced through <span className="font-bold text-white">505 carefully explained programming problems</span>. Understand how code works, not just what it does.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              to="/register"
              className="px-8 py-3.5 bg-white text-blue-700 font-bold rounded-xl text-lg hover:bg-blue-50 transition-colors shadow-lg"
            >
              🚀 Start Learning Free
            </Link>
            <Link
              to="/problems"
              className="px-8 py-3.5 bg-blue-500 text-white font-bold rounded-xl text-lg hover:bg-blue-400 transition-colors border border-blue-400"
            >
              Explore 505 Problems
            </Link>
          </div>
          <div className="mt-8 flex justify-center gap-8 text-blue-200 text-sm">
            <span>✓ 505 Problems</span>
            <span>✓ Live Compiler</span>
            <span>✓ Step-by-step Dry Runs</span>
            <span>✓ Free to use</span>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-16 px-6 bg-gray-50">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">Everything you need to master Python</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((f, i) => (
              <div key={i} className="bg-white rounded-xl p-6 shadow-sm border border-gray-200 hover:shadow-md transition-shadow">
                <f.icon className="text-blue-600 mb-3" size={28} />
                <h3 className="font-semibold text-gray-900 mb-1">{f.title}</h3>
                <p className="text-gray-500 text-sm">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Roadmap */}
      <section className="py-16 px-6">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-4">Learning Roadmap</h2>
          <p className="text-center text-gray-500 mb-10">A complete, structured curriculum from beginner to interview-ready</p>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {phases.map((p) => (
              <div key={p.num} className={`rounded-xl border p-4 ${p.color}`}>
                <div className="flex items-center justify-between mb-1">
                  <span className="text-xs font-bold uppercase tracking-wide opacity-70">Phase {p.num}</span>
                  <span className="text-xs font-medium bg-white bg-opacity-60 rounded-full px-2 py-0.5">{p.count} problems</span>
                </div>
                <p className="font-semibold text-sm">{p.name}</p>
              </div>
            ))}
          </div>
          <div className="text-center mt-8 text-gray-500 text-sm">
            Complete 22-phase roadmap from fundamentals to hard interview dynamic programming.
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-6 bg-blue-600 text-white text-center">
        <h2 className="text-3xl font-bold mb-4">Ready to start solving?</h2>
        <p className="text-blue-100 mb-8 text-lg">Join thousands of students mastering Python problem solving.</p>
        <Link to="/register" className="px-8 py-3.5 bg-white text-blue-700 font-bold rounded-xl text-lg hover:bg-blue-50 transition-colors">
          Get Started — It's Free
        </Link>
      </section>

      <footer className="py-6 text-center text-gray-400 text-sm bg-gray-900">
        © 2026 PySolve Academy · Built for Python learners
      </footer>
    </div>
  );
}

