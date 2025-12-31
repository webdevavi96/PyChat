import React from 'react';
import SkeletonCard from './SkeletonCard';

function Updates() {
  return (
    <div className="flex flex-col gap-4">
      {[...Array(4)].map((_, i) => (
        <SkeletonCard key={i} variant="post" />
      ))}
    </div>
  );
}

export default Updates;
