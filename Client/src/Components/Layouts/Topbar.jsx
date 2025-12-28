import React from "react";
import { NavLink } from "react-router-dom";

function Topbar() {
    const navItem =
        "px-3 py-2 rounded-md text-sm font-medium transition hover:bg-white/10";

    const active =
        "bg-white/15 text-white";

    return (
        <header className="bg-black border-b border-white/10 px-4 py-3">
            <div className="flex items-center justify-between max-w-6xl mx-auto">
                <NavLink
                    to="/home"
                    className="text-lg font-bold tracking-wide text-white"
                >
                    LOGO
                </NavLink>

                <nav>
                    <ul className="flex items-center gap-1">
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
                </nav>
            </div>
        </header>
    );
}

export default Topbar;
