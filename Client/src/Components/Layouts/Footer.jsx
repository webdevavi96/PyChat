import React from "react";
import { NavLink } from "react-router-dom";

function Footer() {
  const linkClass =
    "text-text-secondary hover:text-text-primary transition";

  return (
    <footer className="border-t border-border bg-bg-soft">
      <div
        className="
          max-w-7xl mx-auto
          px-4 py-6
          flex flex-col sm:flex-row items-center justify-between gap-4
          lg:ml-60
        "
      >
        {/* Left */}
        <div className="text-sm text-text-secondary">
          © {new Date().getFullYear()}{" "}
          <span className="font-semibold text-text-primary">PyChat</span>. All
          rights reserved.
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
