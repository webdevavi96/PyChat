import React from 'react';

function Card({ children, title, footer, className = '', padded = true, hoverable = false }) {
  return (
    <div
      className={`bg-surface border-border rounded-xl border ${hoverable ? 'transition-all duration-200 hover:-translate-y-0.5 hover:shadow-xl' : ''} ${className} `}
    >
      {/* Title */}
      {title && (
        <div className="border-border text-text-primary border-b px-5 py-3 font-semibold">
          {title}
        </div>
      )}

      {/* Body */}
      <div className={padded ? 'text-text-secondary p-5' : ''}>{children}</div>

      {/* Footer */}
      {footer && (
        <div className="border-border text-text-muted border-t px-5 py-3 text-sm">{footer}</div>
      )}
    </div>
  );
}

export default Card;
