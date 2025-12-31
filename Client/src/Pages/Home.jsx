import React from 'react';
import { Updates, Chat } from '../Components/Ui/export';

function Home() {
  return (
    <section className="bg-surface min-h-screen w-full p-6">
      <h1 className="text-text-primary mb-4 text-lg font-semibold">Updates from friends</h1>
      <Updates />
    </section>
  );
}

export default Home;
