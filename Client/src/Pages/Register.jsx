import React from 'react';
import { NavLink } from 'react-router-dom';

function Register() {
  return (
    <section className="bg-bg flex min-h-screen w-full items-center justify-center p-6">
      <div className="border-border bg-surface w-full max-w-lg rounded-2xl border p-6 shadow-lg">
        <div className="mb-6 text-center">
          <h1 className="text-text-primary text-2xl font-semibold">Create an account</h1>
          <p className="text-text-secondary mt-1 text-sm">Join us and get started</p>
        </div>
        <form className="space-y-4">
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <label className="text-text-secondary mb-1 block text-sm">First name</label>
              <input
                type="text"
                placeholder="John"
                className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
              />
            </div>

            <div>
              <label className="text-text-secondary mb-1 block text-sm">Last name</label>
              <input
                type="text"
                placeholder="Doe"
                className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
              />
            </div>
          </div>

          <div>
            <label className="text-text-secondary mb-1 block text-sm">Email</label>
            <input
              type="email"
              placeholder="you@example.com"
              className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
            />
          </div>

          <div>
            <label className="text-text-secondary mb-1 block text-sm">Phone</label>
            <input
              type="tel"
              placeholder="+91 98765 43210"
              className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
            />
          </div>

          <div>
            <label className="text-text-secondary mb-1 block text-sm">Password</label>
            <input
              type="password"
              placeholder="••••••••"
              className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
            />
          </div>

          <div>
            <label className="text-text-secondary mb-1 block text-sm">Confirm password</label>
            <input
              type="password"
              placeholder="••••••••"
              className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
            />
          </div>

          <label className="text-text-secondary flex items-start gap-2 text-sm">
            <input type="checkbox" className="accent-brand mt-1" />
            <span>
              I agree to the{' '}
              <NavLink to="/terms" className="text-brand hover:underline">
                Terms & Conditions
              </NavLink>
            </span>
          </label>

          <button
            type="submit"
            className="bg-brand hover:bg-brand-soft focus:ring-brand/50 mt-2 w-full rounded-lg px-4 py-2 font-medium text-white focus:ring-2 focus:outline-none"
          >
            Create Account
          </button>
        </form>
        +{' '}
        <div className="text-text-secondary mt-6 text-center text-sm">
          Already have an account?{' '}
          <NavLink to="/login" className="text-brand hover:underline">
            Sign in
          </NavLink>
        </div>
      </div>
    </section>
  );
}

export default Register;
