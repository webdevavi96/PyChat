import React from 'react';
import { Outlet, useParams } from 'react-router-dom';
import ChatList from './ChatList';

function Chat() {
  const { id } = useParams();

  return (
    <section className="bg-bg min-h-screen w-full">
      <div className="border-border bg-surface mx-auto flex h-screen max-w-6xl border">
        <ChatList />

        <div className="hidden flex-1 md:flex">
          {id ? (
            <Outlet />
          ) : (
            <div className="text-text-muted flex flex-1 items-center justify-center">
              Select a chat to start messaging
            </div>
          )}
        </div>

        <div className="md:hidden">
          <Outlet />
        </div>
      </div>
    </section>
  );
}

export default Chat;
