import React from 'react';

const VARIANTS = {
  friend: {
    avatar: true,
    titleWidth: 'w-1/3',
    rows: 1,
    actions: true,
  },
  post: {
    avatar: true,
    titleWidth: 'w-1/4',
    rows: 3,
    actions: false,
  },
  service: {
    avatar: false,
    titleWidth: 'w-1/2',
    rows: 2,
    actions: true,
  },
  profile: {
    avatar: true,
    titleWidth: 'w-1/4',
    rows: 2,
    actions: true,
  },
};

function SkeletonCard({ variant = 'post', className = '' }) {
  const { avatar, titleWidth, rows, actions } = VARIANTS[variant] || VARIANTS.post;

  return (
    <div className={`border-border bg-surface animate-pulse rounded-xl border ${className}`}>
      <div className="p-5">
        <div className="flex items-start gap-4">
          {avatar && <div className="bg-surface-elevated h-16 w-16 rounded-full" />}

          <div className="flex-1 space-y-3">
            <div className={`bg-surface-elevated h-4 rounded ${titleWidth}`} />
            {[...Array(rows)].map((_, i) => (
              <div key={i} className="bg-surface-elevated h-3 w-full rounded" />
            ))}
          </div>
        </div>

        {actions && (
          <div className="mt-4 flex gap-2">
            <div className="bg-surface-elevated h-8 w-24 rounded" />
            <div className="bg-surface-elevated h-8 w-20 rounded" />
          </div>
        )}
      </div>
    </div>
  );
}

export default SkeletonCard;
