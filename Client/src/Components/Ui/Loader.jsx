import React from "react";

function Loader({ label = "Loading..." }) {
  return (
    <div className="flex flex-col items-center justify-center gap-4 py-10">

      {/* Ring */}
      <div className="relative h-12 w-12">
        <span className="absolute inset-0 rounded-full border-2 border-border"></span>
        <span className="absolute inset-0 rounded-full border-2 border-brand border-t-transparent animate-spin"></span>
      </div>

      {/* Text */}
      <p className="text-sm text-text-muted tracking-wide">
        {label}
      </p>
    </div>
  );
};


function DotLoader() {
  return (
    <div className="flex items-center gap-2">
      {[0, 1, 2].map((i) => (
        <span
          key={i}
          className="h-2 w-2 rounded-full bg-brand animate-bounce"
          style={{ animationDelay: `${i * 0.15}s` }}
        />
      ))}
    </div>
  );
};



export { Loader, DotLoader };
