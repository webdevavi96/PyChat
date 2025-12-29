import React, { useContext } from "react";
import { NavLink } from "react-router-dom";
import { AuthContext } from "../../Contexts/authContext";
import { Button } from "../Ui/export.js";

function Topbar() {

    const { isAuthenticated } = useContext(AuthContext);


    const baseItem =
        "px-3 py-2 rounded-md text-sm font-medium transition-all duration-200";

    const inactive =
        "text-text-secondary hover:bg-white/5 hover:text-text-primary";

    const active =
        "bg-surface-elevated text-text-primary";

    return (
        <header className="bg-bg-soft border-b border-border px-4 py-3">
            <div className="flex items-center justify-between max-w-6xl mx-auto">

                {/* Logo */}
                <NavLink
                    to="/home"
                    className="text-lg font-bold tracking-wide text-text-primary"
                >
                    PyChat
                </NavLink>

                {/* Nav */}
                <nav>
                    {isAuthenticated && (<ul className="flex items-center gap-1">
                        {[
                            { to: "/home", label: "Home" },
                            { to: "/chat", label: "Chat" },
                            { to: "/friends", label: "Friends" },
                            { to: "/profile", label: "Profile" },
                            { to: "/settings", label: "Settings" },
                        ].map((item) => (
                            <li key={item.to}>
                                <NavLink
                                    to={item.to}
                                    className={({ isActive }) =>
                                        `${baseItem} ${isActive ? active : inactive}`
                                    }
                                >
                                    {item.label}
                                </NavLink>
                            </li>
                        ))}
                    </ul>)}

                    {!isAuthenticated && (
                        <div className="flex gap-4">
                            <Button variant="primary" title="Sign In" />
                            <Button variant="outline" title="Sign Up" />
                        </div>
                    )}

                </nav>
            </div>
        </header>
    );
}

export default Topbar;
