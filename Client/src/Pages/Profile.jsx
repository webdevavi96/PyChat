import React from 'react';
import { SkeletonCard } from '../Components/Ui/export';

function Profile() {
  return (
    <section className="bg-bg min-h-screen w-full p-6">
      <div className="mx-auto max-w-5xl space-y-8">
        <h1 className="text-text-primary text-xl font-semibold">Your Profile</h1>

        <SkeletonCard variant="profile" />

        <div className="border-border border-t" />

        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
          {[...Array(9)].map((_, i) => (
            <SkeletonCard key={i} variant="post" className="aspect-square" />
          ))}
        </div>
      </div>
    </section>
  );
}

export default Profile;
