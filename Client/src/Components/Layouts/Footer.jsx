import React from 'react';
import { NavLink } from 'react-router-dom';

function Footer() {
  const linkClass = 'text-text-secondary hover:text-text-primary transition';

  return (
    <footer className="border-border bg-bg-soft border-t">
      <div className="mx-auto flex max-w-7xl flex-col items-center justify-between gap-4 px-4 py-6 sm:flex-row lg:ml-60">
        {/* Left */}
        <div className="text-text-secondary text-sm">
          © {new Date().getFullYear()}{' '}
          <span className="text-text-primary font-semibold">PyChat</span>. All rights reserved.
        </div>

        {/* Right */}
        <div className="flex items-center gap-6 text-sm">
          <NavLink to="/privacy" className={linkClass}>
            Privacy & Policy
          </NavLink>

          <NavLink to="/terms" className={linkClass}>
            Terms & Conditions
          </NavLink>

          <NavLink to="/policy" className={linkClass}>
            Cookies & Uses
          </NavLink>

          <NavLink to="/security" className={linkClass}>
            Safty & Security
          </NavLink>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
