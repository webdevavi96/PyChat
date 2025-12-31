import React from 'react';
import { Button, Card } from '../Components/Ui/export.js';

function Landing() {
  return (
    <div className="bg-bg text-text-primary flex min-h-screen w-full flex-col justify-between">
      <section className="mb-4 flex flex-col items-center px-6 pt-24 text-center">
        <h1 className="mb-4 text-4xl font-bold tracking-tight md:text-5xl">
          Welcome to <span className="text-accent">PyChat</span>
        </h1>

        <p className="text-text-secondary mb-10 max-w-2xl text-lg md:text-xl">
          India’s modern, secure, and fast messaging platform built for real-time conversations.
        </p>

        <div className="flex gap-4">
          <Button variant="primary" title="Sign In" />
          <Button variant="outline" title="Sign Up" />
        </div>
      </section>

      <section className="bg-bg-soft px-6 py-20">
        <div className="mx-auto max-w-5xl">
          <h2 className="mb-10 text-center text-2xl font-semibold">Why Choose PyChat?</h2>

          <div className="grid gap-6 md:grid-cols-3">
            {[
              {
                title: 'End-to-End Encryption',
                desc: 'Your messages are protected with industry-standard security.',
              },
              {
                title: '24×7 Support',
                desc: 'Always available assistance from our expert support team.',
              },
              {
                title: 'User-Driven Improvements',
                desc: 'Monthly feedback cycles that actually ship improvements.',
              },
            ].map((item, i) => (
              <Card key={i} title={item.title} hoverable className="h-full">
                <p className="text-text-secondary">{item.desc}</p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      <section className="px-6 py-12 text-center">
        <p className="text-text-secondary mb-4">Ready to start chatting securely?</p>

        <Button variant="secondary" title="Join PyChat" size="lg" />
      </section>
    </div>
  );
}

export default Landing;
