import React from 'react';

function Loader({ label = 'Loading...' }) {
  return (
    <div className="flex flex-col items-center justify-center gap-4 py-10">
      <div className="relative h-12 w-12">
        <span className="border-border absolute inset-0 rounded-full border-2"></span>
        <span className="border-brand absolute inset-0 animate-spin rounded-full border-2 border-t-transparent"></span>
      </div>
      <p className="text-text-muted text-sm tracking-wide">{label}</p>
    </div>
  );
}

function DotLoader() {
  return (
    <div className="flex items-center gap-2">
      {[0, 1, 2].map((i) => (
        <span
          key={i}
          className="bg-brand h-2 w-2 animate-bounce rounded-full"
          style={{ animationDelay: `${i * 0.15}s` }}
        />
      ))}
    </div>
  );
}

export { Loader, DotLoader };
