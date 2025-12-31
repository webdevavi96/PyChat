import React from 'react';
import { useNavigate } from 'react-router-dom';

function ChatPage() {
  const navigate = useNavigate();

  return (
    <div className="flex h-full flex-1 flex-col">
      <div className="border-border flex items-center gap-3 border-b p-4">
        <button onClick={() => navigate(-1)} className="text-text-secondary md:hidden">
          ←
        </button>

        <div className="bg-surface-elevated h-10 w-10 rounded-full" />
        <div>
          <div className="text-text-primary text-sm font-medium">Username</div>
          <div className="text-text-muted text-xs">Active now</div>
        </div>
      </div>

      <div className="flex-1 space-y-4 overflow-y-auto p-4">
        <div className="flex justify-start">
          <div className="bg-surface-elevated max-w-xs rounded-2xl px-4 py-2 text-sm">Hello!</div>
        </div>

        <div className="flex justify-end">
          <div className="bg-brand max-w-xs rounded-2xl px-4 py-2 text-sm text-white">Hi 👋</div>
        </div>
      </div>

      <div className="border-border border-t p-4">
        <div className="border-border bg-bg-soft flex items-center gap-2 rounded-full border px-4 py-2">
          <input
            type="text"
            placeholder="Message..."
            className="flex-1 bg-transparent text-sm focus:outline-none"
          />
          <button className="text-brand font-medium">Send</button>
        </div>
      </div>
    </div>
  );
}

export default ChatPage;
