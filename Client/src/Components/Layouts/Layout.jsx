import React from 'react';
import { Outlet } from 'react-router-dom';
import Topbar from './Topbar';
import Footer from './Footer';
import Sidebar from './Sidebar';

function Layout() {
  return (
    <div className="spy-grid scanlines relative flex min-h-screen w-full flex-col overflow-hidden bg-black text-white">
      <div className="fixed top-0 left-0 z-50 w-full lg:hidden">
        <Topbar />
      </div>

      <div className="flex flex-1 pt-14 lg:pt-0">
        <aside className="hidden w-60 lg:fixed lg:inset-y-0 lg:left-0 lg:z-40 lg:block">
          <Sidebar />
        </aside>

        <main className="mx-auto w-full max-w-7xl flex-1 px-4 py-6 lg:ml-60">
          <Outlet />
        </main>
      </div>

      <Footer />
    </div>
  );
}

export default Layout;
