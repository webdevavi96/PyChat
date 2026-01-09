import React, { useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { register } from "../Services/auth/authServices"
import { AiFillEye, AiFillEyeInvisible } from "react-icons/ai";


function Register() {
  const [showPass, setShowPass] = useState(false);
  const navigate = useNavigate();

  const handleForm = async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());

    if (data.password !== data.confirm_password) {
      alert("Passwords do not match");
      return;
    }

    if (!data.terms) {
      alert("Accept the terms");
      return;
    }

    delete data.confirm_password;
    delete data.terms;

    try {
      const res = await register(data);
      if (res.status == 200) {
        sessionStorage.setItem("pending_email", data.email);
        navigate("/verify_otp")
      }
      else alert("Something went wrong! Please try again later.")
    } catch (err) {
      alert("Something went wrong! Please try again later.")
    }
  };



  return (
    <section className="bg-bg flex min-h-screen w-full items-center justify-center p-6">
      <div className="border-border bg-surface w-full max-w-lg rounded-2xl border p-6 shadow-lg">
        <div className="mb-6 text-center">
          <h1 className="text-text-primary text-2xl font-semibold">Create an account</h1>
          <p className="text-text-secondary mt-1 text-sm">Join us and get started</p>
        </div>
        <form className="space-y-4" onSubmit={handleForm}>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <label className="text-text-secondary mb-1 block text-sm">First name</label>
              <input
                name='first_name'
                type="text"
                placeholder="John"
                className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
              />
            </div>

            <div>
              <label className="text-text-secondary mb-1 block text-sm">Last name</label>
              <input
                name='last_name'
                type="text"
                placeholder="Doe"
                className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
              />
            </div>
          </div>

          <div>
            <label className="text-text-secondary mb-1 block text-sm">Email</label>
            <input
              name='email'
              type="email"
              placeholder="you@example.com"
              className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
            />
          </div>

          <div>
            <label className="text-text-secondary mb-1 block text-sm">Phone</label>
            <input
              name='phone'
              type="tel"
              placeholder="+91 98765 43210"
              className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
            />
          </div>

          <div>
            <label className="text-text-secondary mb-1 block text-sm">Gender</label>
            <select
              name="gender"
              required
              className="border-border bg-bg-soft text-text-primary focus:ring-brand/40 w-full rounded-lg border px-4 py-2 focus:ring-2 focus:outline-none"
            >
              <option value="">Select gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>


          <div className="space-y-4">
            <div>
              <label className="text-text-secondary mb-1 block text-sm">
                Password
              </label>

              <div className="relative">
                <input
                  name="password"
                  type={showPass ? "text" : "password"}
                  placeholder="••••••••"
                  className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 pr-10 focus:ring-2 focus:outline-none"
                />

                <button
                  type="button"
                  onClick={() => setShowPass(!showPass)}
                  className="text-text-muted hover:text-text-primary absolute right-3 top-1/2 -translate-y-1/2"
                >
                  <AiFillEye />
                </button>
              </div>
            </div>

            {/* Confirm Password */}
            <div>
              <label className="text-text-secondary mb-1 block text-sm">
                Confirm Password
              </label>

              <div className="relative">
                <input
                  name="confirm_password"
                  type={showPass ? "text" : "password"}
                  placeholder="••••••••"
                  className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 pr-10 focus:ring-2 focus:outline-none"
                />

                <button
                  type="button"
                  onClick={() => setShowPass(!showPass)}
                  className="text-text-muted hover:text-text-primary absolute right-3 top-1/2 -translate-y-1/2"
                >
                  <AiFillEye />
                </button>
              </div>
            </div>
          </div>


          <label className="text-text-secondary flex items-start gap-2 text-sm">
            <input
              name='terms' type="checkbox" className="accent-brand mt-1" />
            <span>
              I agree to the{' '}
              <NavLink to="/terms" className="text-brand hover:underline">
                Terms & Conditions
              </NavLink>
            </span>
          </label>

          <button
            type='Submit'
            className="bg-brand hover:bg-brand-soft focus:ring-brand/50 mt-2 w-full rounded-lg px-4 py-2 font-medium text-white focus:ring-2 focus:outline-none"
          >
            Create Account
          </button>
        </form>
        {' '}
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
