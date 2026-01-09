import React from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { verify_otp } from "../Services/auth/authServices";

function OTPVerification() {
    const navigate = useNavigate();

    const handleForm = async (e) => {
        e.preventDefault();

        const formData = new FormData(e.target);
        const otp = formData.get("otp");

        if (!otp || otp.length !== 6) {
            alert("Please enter a valid 6-digit OTP");
            return;
        }

        try {
            const res = await verify_otp(otp);

            if (res.status === 200) {
                sessionStorage.removeItem("pending_email");
                navigate("/login");
            } else {
                alert("Invalid OTP. Please try again.");
            }
        } catch (error) {
            console.error(error);
            alert("OTP verification failed. Please try again.");
        }
    };

    return (
        <section className="bg-bg flex min-h-screen w-full items-center justify-center p-6">
            <div className="border-border bg-surface w-full max-w-md rounded-2xl border p-6 shadow-lg">
                <div className="mb-6 text-center">
                    <h1 className="text-text-primary text-2xl font-semibold">
                        Verify your email
                    </h1>
                    <p className="text-text-secondary mt-1 text-sm">
                        Enter the 6-digit OTP sent to your email
                    </p>
                </div>

                <form className="space-y-4" onSubmit={handleForm}>
                    <div>
                        <label className="text-text-secondary mb-1 block text-sm">
                            One Time Password
                        </label>

                        <input
                            type="text"
                            name="otp"
                            inputMode="numeric"
                            maxLength={6}
                            placeholder="••••••"
                            className="border-border bg-bg-soft text-text-primary placeholder:text-text-muted focus:ring-brand/40 w-full rounded-lg border px-4 py-2 text-center tracking-widest focus:ring-2 focus:outline-none"
                        />
                    </div>

                    <button
                        type="submit"
                        className="bg-brand hover:bg-brand-soft focus:ring-brand/50 mt-2 w-full rounded-lg px-4 py-2 font-medium text-white focus:ring-2 focus:outline-none"
                    >
                        Verify OTP
                    </button>
                </form>

                <div className="text-text-secondary mt-6 flex items-center justify-between text-sm">
                    <span>Didn’t receive the code?</span>
                    <button type="button" className="text-brand hover:underline">
                        Resend OTP
                    </button>
                </div>

                <div className="text-text-secondary mt-4 text-center text-sm">
                    Back to{" "}
                    <NavLink to="/login" className="text-brand hover:underline">
                        Login
                    </NavLink>
                </div>
            </div>
        </section>
    );
}

export default OTPVerification;
