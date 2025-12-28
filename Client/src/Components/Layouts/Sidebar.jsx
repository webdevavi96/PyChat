import React from "react";
import { NavLink } from "react-router-dom";

function Sidebar() {
    const navItem =
        "flex items-center px-4 py-3 rounded-lg transition hover:bg-white/10";

    const active =
        "bg-white/15 text-white font-semibold";

    return (
        <aside className="h-full w-60 bg-black border-r border-white/10 px-4 py-6">
            {/* Logo */}
            <div className="mb-10 text-xl font-bold tracking-wide">
                <NavLink to="/home" className="text-white">
                    LOGO
                </NavLink>
            </div>

            {/* Navigation */}
            <ul className="space-y-2">
                <li>
                    <NavLink
                        to="/home"
                        className={({ isActive }) =>
                            `${navItem} ${isActive ? active : "text-gray-300"}`
                        }
                    >
                        Home
                    </NavLink>
                </li>

                <li>
                    <NavLink
                        to="/chat"
                        className={({ isActive }) =>
                            `${navItem} ${isActive ? active : "text-gray-300"}`
                        }
                    >
                        Chat
                    </NavLink>
                </li>

                <li>
                    <NavLink
                        to="/friends"
                        className={({ isActive }) =>
                            `${navItem} ${isActive ? active : "text-gray-300"}`
                        }
                    >
                        Friends
                    </NavLink>
                </li>

                <li>
                    <NavLink
                        to="/profile"
                        className={({ isActive }) =>
                            `${navItem} ${isActive ? active : "text-gray-300"}`
                        }
                    >
                        Profile
                    </NavLink>
                </li>

                <li>
                    <NavLink
                        to="/settings"
                        className={({ isActive }) =>
                            `${navItem} ${isActive ? active : "text-gray-300"}`
                        }
                    >
                        Settings
                    </NavLink>
                </li>
            </ul>
        </aside>
    );
}

export default Sidebar;
