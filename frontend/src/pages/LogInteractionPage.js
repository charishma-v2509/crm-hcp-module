import React from 'react';
import Header from '../components/Header';
import InteractionForm from '../components/InteractionForm';
import ChatPanel from '../components/ChatPanel';

function LogInteractionPage() {
  return (
    <div>
      <Header />
      <div className="main-layout">
        <InteractionForm />
        <ChatPanel />
      </div>
    </div>
  );
}

export default LogInteractionPage;