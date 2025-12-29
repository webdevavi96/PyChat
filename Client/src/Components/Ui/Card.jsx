import React from "react";

function Card({
    children,
    title,
    footer,
    className = "",
    padded = true,
    hoverable = false,
}) {
    return (
        <div
            className={`
        bg-surface border border-border rounded-xl
        ${hoverable ? "transition-all duration-200 hover:shadow-xl hover:-translate-y-0.5" : ""}
        ${className}
      `}
        >
            {/* Title */}
            {title && (
                <div className="border-b border-border px-5 py-3 font-semibold text-text-primary">
                    {title}
                </div>
            )}

            {/* Body */}
            <div className={padded ? "p-5 text-text-secondary" : ""}>
                {children}
            </div>

            {/* Footer */}
            {footer && (
                <div className="border-t border-border px-5 py-3 text-sm text-text-muted">
                    {footer}
                </div>
            )}
        </div>
    );
}

export default Card;
