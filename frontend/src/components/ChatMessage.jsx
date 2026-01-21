import React from 'react';

function ChatMessage({ message }) {
    const { role, content, isError } = message;

    return (
        <div className={`message ${role}`}>
            <div className="message-avatar">
                {role === 'user' ? '👤' : '🤖'}
            </div>
            <div className={`message-content ${isError ? 'error' : ''}`}>
                {content}
            </div>
        </div>
    );
}

export default ChatMessage;
