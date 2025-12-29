import React from "react";
import { Button, Card } from "../Components/Ui/export.js";

function Landing() {
  return (
    <div className="min-h-screen w-full bg-bg text-text-primary flex flex-col justify-between">

      {/* Hero */}
      <section className="flex flex-col items-center text-center px-6 pt-24 mb-4">
        <h1 className="text-4xl md:text-5xl font-bold mb-4 tracking-tight">
          Welcome to <span className="text-accent">PyChat</span>
        </h1>

        <p className="text-lg md:text-xl max-w-2xl mb-10 text-text-secondary">
          India’s modern, secure, and fast messaging platform built for real-time conversations.
        </p>

        <div className="flex gap-4">
          <Button variant="primary" title="Sign In" />
          <Button variant="outline" title="Sign Up" />
        </div>
      </section>

      {/* Features */}
      <section className="bg-bg-soft py-20 px-6">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-2xl font-semibold mb-10 text-center">
            Why Choose PyChat?
          </h2>

          <div className="grid md:grid-cols-3 gap-6">
            {[
              {
                title: "End-to-End Encryption",
                desc: "Your messages are protected with industry-standard security.",
              },
              {
                title: "24×7 Support",
                desc: "Always available assistance from our expert support team.",
              },
              {
                title: "User-Driven Improvements",
                desc: "Monthly feedback cycles that actually ship improvements.",
              },
            ].map((item, i) => (
              <Card
                key={i}
                title={item.title}
                hoverable
                className="h-full"
              >
                <p className="text-text-secondary">
                  {item.desc}
                </p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Footer CTA */}
      <section className="text-center py-12 px-6">
        <p className="text-text-secondary mb-4">
          Ready to start chatting securely?
        </p>

        <Button variant="secondary" title="Join PyChat" size="lg" />
      </section>
    </div>
  );
}

export default Landing;
  