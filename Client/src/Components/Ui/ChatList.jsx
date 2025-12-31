import React from 'react';
import { useNavigate } from 'react-router-dom';

function ChatList() {
  const navigate = useNavigate();

  return (
    <aside className="border-border w-full border-r md:w-80">
      <div className="border-border border-b p-4">
        <h2 className="text-text-primary text-lg font-semibold">Messages</h2>
      </div>

      <div className="space-y-1 p-2">
        {[...Array(8)].map((_, i) => (
          <button
            key={i}
            onClick={() => navigate(`/chat/${i}`)}
            className="hover:bg-surface-elevated flex w-full items-center gap-3 rounded-lg p-2 text-left"
          >
            <div className="bg-surface-elevated h-10 w-10 rounded-full" />
            <div className="flex-1">
              <div className="text-text-primary text-sm font-medium">Username</div>
              <div className="text-text-muted truncate text-xs">Last message preview…</div>
            </div>
          </button>
        ))}
      </div>
    </aside>
  );
}

export default ChatList;
