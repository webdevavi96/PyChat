import React from 'react';
import { NavLink } from 'react-router-dom';

function Login() {
  return (
    <section className="bg-bg flex min-h-screen w-full items-center justify-center p-6">
      <div className="border-border bg-surface w-full max-w-md rounded-2xl border p-6 shadow-lg">
        <div className="mb-6 text-center">
          <h1 className="text-text-primary text-2xl font-semibold">Welcome back</h1>
          <p className="text-text-secondary mt-1 text-sm">Sign in to continue</p>
        </div>

        <form className="space-y-4">
          <div>
            <label className="text-text-secondary mb-1 block text-sm">Email</label>
            <input
              type="email"
              placeholder="you@example.com"
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

          <div className="flex items-center justify-between text-sm">
            <label className="text-text-secondary flex items-center gap-2">
              <input type="checkbox" className="accent-brand" />
              Remember me
            </label>

            <button type="button" className="text-brand hover:underline">
              Forgot password?
            </button>
          </div>

          <button
            type="submit"
            className="bg-brand hover:bg-brand-soft focus:ring-brand/50 mt-2 w-full rounded-lg px-4 py-2 font-medium text-white focus:ring-2 focus:outline-none"
          >
            Sign In
          </button>
        </form>

        <div className="text-text-secondary mt-6 text-center text-sm">
          Don’t have an account?{' '}
          <NavLink to="/register" className="text-brand hover:underline">
            Sign up
          </NavLink>
        </div>
      </div>
    </section>
  );
}

export default Login;
