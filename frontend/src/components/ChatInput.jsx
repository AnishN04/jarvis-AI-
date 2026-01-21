import React, { useState } from 'react';

function ChatInput({ onSendMessage, disabled }) {
    const [inputValue, setInputValue] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (inputValue.trim() && !disabled) {
            onSendMessage(inputValue);
            setInputValue('');
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
        }
    };

    return (
        <div className="input-area">
            <form onSubmit={handleSubmit} className="input-wrapper">
                <textarea
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    onKeyDown={handleKeyDown}
                    placeholder="Type your message here..."
                    rows="1"
                    disabled={disabled}
                    className="user-input"
                />
                <button
                    type="submit"
                    className="send-button"
                    disabled={disabled || !inputValue.trim()}
                >
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <line x1="22" y1="2" x2="11" y2="13"></line>
                        <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                    </svg>
                </button>
            </form>
            <div className="input-hint">
                Press <kbd>Enter</kbd> to send • <kbd>Shift + Enter</kbd> for new line
            </div>
        </div>
    );
}

export default ChatInput;
