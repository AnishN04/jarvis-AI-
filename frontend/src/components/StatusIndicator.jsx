import React from 'react';

function StatusIndicator({ status }) {
    const getStatusText = () => {
        switch (status) {
            case 'connected':
                return 'Connected';
            case 'warning':
                return 'Server running, LLM offline';
            case 'error':
                return 'Server offline';
            default:
                return 'Connecting...';
        }
    };

    return (
        <div className="status-indicator">
            <div className={`status-dot ${status}`}></div>
            <span>{getStatusText()}</span>
        </div>
    );
}

export default StatusIndicator;
