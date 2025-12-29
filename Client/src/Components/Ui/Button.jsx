import React from "react";

function Button({
    variant = "primary",
    title = "Button",
    onClick = () => { },
    type = "button",
    size = "md",
    disabled = false,
    loading = false,
    className = "",
}) {
    const variants = {
        primary:
            "bg-brand hover:bg-brand-soft text-white shadow-lg hover:shadow-brand/40",

        secondary:
            "bg-accent text-black hover:brightness-110 shadow-md",

        outline:
            "border border-border text-text-primary hover:bg-white/5",

        danger:
            "bg-error text-white hover:brightness-110",

        success:
            "bg-success text-white hover:brightness-110",
    };

    const sizes = {
        sm: "px-3 py-1.5 text-sm",
        md: "px-4 py-2 text-base",
        lg: "px-6 py-3 text-lg",
    };

    return (
        <button
            type={type}
            onClick={onClick}
            disabled={disabled || loading}
            className={`
        inline-flex items-center justify-center gap-2
        rounded-lg font-semibold transition-all duration-200
        focus:outline-none focus:ring-2 focus:ring-brand/50 focus:ring-offset-2 focus:ring-offset-bg
        ${variants[variant] || variants.primary}
        ${sizes[size] || sizes.md}
        ${disabled || loading ? "opacity-50 cursor-not-allowed" : ""}
        ${className}
      `}
        >
            {loading && (
                <span className="h-4 w-4 animate-spin rounded-full border-2 border-white/70 border-t-transparent" />
            )}
            {title}
        </button>
    );
}

export default Button;
