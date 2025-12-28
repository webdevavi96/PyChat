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
        bg-white rounded-xl border border-gray-200 shadow-sm
        ${hoverable ? "transition hover:shadow-lg hover:-translate-y-1" : ""}
        ${className}
      `}
        >
            {title && (
                <div className="border-b px-5 py-3 font-semibold text-gray-800">
                    {title}
                </div>
            )}

            <div className={padded ? "p-5" : ""}>
                {children}
            </div>

            {footer && (
                <div className="border-t px-5 py-3 text-sm text-gray-600">
                    {footer}
                </div>
            )}
        </div>
    );
}

export default Card;
