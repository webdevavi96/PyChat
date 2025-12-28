import React from "react";
import { Outlet } from "react-router-dom";
import Topbar from "./Topbar";
import Footer from "./Footer";
import Sidebar from "./Sidebar";

function Layout() {
    return (
        <div className="min-h-screen w-full bg-black text-white relative overflow-hidden spy-grid scanlines">
            <div className="lg:hidden fixed top-0 left-0 w-full z-50">
                <Topbar />
            </div>

            <div className="flex relative z-10">
                <aside className="hidden lg:fixed lg:inset-y-0 lg:left-0 lg:z-40 lg:block lg:w-60">
                    <Sidebar />
                </aside>

                <main
                    className="
            flex-1
            pt-16 lg:pt-6
            px-4
            pb-20
            lg:pl-60
            max-w-6xl
            mx-auto
          "
                >
                    <Outlet />
                </main>
            </div>

            <Footer />
        </div>
    );
}

export default Layout;
