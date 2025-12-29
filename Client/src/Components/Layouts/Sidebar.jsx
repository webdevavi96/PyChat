import React, { useContext } from "react";
import { NavLink } from "react-router-dom";
import { Button } from "../Ui/export.js";
import { AuthContext } from "../../Contexts/authContext";

function Sidebar() {

    const { isAuthenticated } = useContext(AuthContext);

    const baseItem =
        "flex items-center px-4 py-3 rounded-lg transition-all duration-200";

    const inactive =
        "text-text-secondary hover:bg-white/5 hover:text-text-primary";

    const active =
        "bg-surface-elevated text-text-primary font-semibold shadow-md";


    return (
        <aside className="h-full w-60 bg-bg-soft border-r border-border px-4 py-6">

            {/* Logo */}
            <div className="mb-10 text-xl font-bold tracking-wide">
                <NavLink to="/home" className="text-text-primary">
                    PyChat
                </NavLink>
            </div>

            {isAuthenticated && (<ul className="space-y-2">
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
                <div className="flex flex-col gap-4">
                    <Button variant="primary" title="Sign In" />
                    <Button variant="outline" title="Sign Up" />
                </div>
            )}

        </aside>
    );
}

export default Sidebar;
