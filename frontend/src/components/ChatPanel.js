import React, { useState, useRef, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addChatMessage } from '../store/interactionSlice';
import { sendChatMessage } from '../api/api';

function ChatPanel() {
  const dispatch = useDispatch();
  const { chatMessages, currentInteraction } = useSelector(
    (state) => state.interaction
  );
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', text: input };
    dispatch(addChatMessage(userMessage));
    setInput('');
    setLoading(true);

    try {
      const response = await sendChatMessage({
        message: input,
        hcp_id: currentInteraction.hcp_id || null,
      });

      const aiText =
        response.response ||
        response.suggestions ||
        response.ai_summary ||
        JSON.stringify(response.data) ||
        'Done!';

      dispatch(addChatMessage({ role: 'ai', text: aiText }));
    } catch (error) {
      dispatch(
        addChatMessage({
          role: 'ai',
          text: 'Sorry, something went wrong. Please try again.',
        })
      );
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') handleSend();
  };

  return (
    <div className="chat-card">
      <h2>🤖 AI Assistant</h2>
      <p>Log interaction via chat</p>

      <div className="chat-messages">
        {chatMessages.map((msg, index) => (
          <div
            key={index}
            className={`chat-bubble ${msg.role === 'user' ? 'user' : 'ai'}`}
          >
            {msg.text}
          </div>
        ))}
        {loading && (
          <div className="chat-bubble ai">Thinking...</div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="chat-input-row">
        <input
          type="text"
          placeholder="Describe interaction..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button className="chat-send-btn" onClick={handleSend}>
          Log
        </button>
      </div>
    </div>
  );
}

export default ChatPanel;