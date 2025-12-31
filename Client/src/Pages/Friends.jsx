import React from 'react';
import { SkeletonCard } from '../Components/Ui/export.js';

function Friends() {
  return (
    <section className="bg-bg-soft min-h-screen p-6">
      {/* Header */}
      <div className="mb-6 flex items-center justify-between">
        <h1 className="text-text-primary text-xl font-semibold">Friends</h1>
        <button className="border-border text-text-secondary hover:bg-surface rounded-lg border px-3 py-2 text-sm">
          Add Friend
        </button>
      </div>

      {/* Search */}
      <div className="mb-4">
        <input
          type="text"
          placeholder="Search friends"
          className="border-border bg-surface text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
        />
      </div>

      {/* Tabs */}
      <div className="mb-6 flex gap-2">
        {['All', 'Requests', 'Suggestions', 'Blocked'].map((tab) => (
          <button
            key={tab}
            className="border-border text-text-secondary hover:bg-surface rounded-full border px-4 py-1.5 text-sm"
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Content */}
      <div className="border-border bg-surface rounded-xl border p-6">
        {/* Empty State */}
        <div className="flex flex-col items-center justify-center gap-2 py-12">
          <div className="bg-surface-elevated h-10 w-10 rounded-full" />
          <p className="text-text-secondary text-sm">Your friends will appear here</p>
        </div>

        {/* Skeleton List */}
        <div className="mt-6 space-y-4">
          {[...Array(3)].map((_, i) => (
            <SkeletonCard key={i} variant="friend" />
          ))}
        </div>
      </div>
    </section>
  );
}

export default Friends;
