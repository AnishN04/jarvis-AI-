import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css';
import ChatMessage from './components/ChatMessage';
import ChatInput from './components/ChatInput';
import StatusIndicator from './components/StatusIndicator';

const API_URL = ''; // Uses proxy from package.json in dev

function App() {
    const [messages, setMessages] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [connectionStatus, setConnectionStatus] = useState('connecting');
    const chatContainerRef = useRef(null);

    // Check server status on mount and periodically
    useEffect(() => {
        checkServerStatus();
        const interval = setInterval(checkServerStatus, 30000);
        return () => clearInterval(interval);
    }, []);

    // Auto-scroll to bottom when new messages arrive
    useEffect(() => {
        if (chatContainerRef.current) {
            chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
    }, [messages, isLoading]);

    const checkServerStatus = async () => {
        try {
            const response = await axios.get(`${API_URL}/health`);
            if (response.data.status === 'running' && response.data.llm_loaded) {
                setConnectionStatus('connected');
            } else if (response.data.status === 'running') {
                setConnectionStatus('warning');
            } else {
                setConnectionStatus('error');
            }
        } catch (error) {
            setConnectionStatus('error');
        }
    };

    const sendMessage = async (messageText) => {
        if (!messageText.trim() || isLoading) return;

        // Add user message
        const userMessage = {
            role: 'user',
            content: messageText,
            timestamp: new Date().toISOString()
        };
        setMessages(prev => [...prev, userMessage]);

        // Set loading state
        setIsLoading(true);

        try {
            const response = await axios.post(`${API_URL}/chat`, {
                message: messageText
            });

            // Add assistant response
            const assistantMessage = {
                role: 'assistant',
                content: response.data.response,
                timestamp: new Date().toISOString()
            };
            setMessages(prev => [...prev, assistantMessage]);
        } catch (error) {
            // Add error message
            const errorMessage = {
                role: 'assistant',
                content: 'Sorry, I could not connect to the server. Please make sure the backend is running.',
                timestamp: new Date().toISOString(),
                isError: true
            };
            setMessages(prev => [...prev, errorMessage]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="app">
            <div className="container">
                {/* Header */}
                <div className="header">
                    <div className="logo">
                        <div className="logo-icon">🤖</div>
                        <h1>JARVIS</h1>
                    </div>
                    <StatusIndicator status={connectionStatus} />
                </div>

                {/* Chat Container */}
                <div className="chat-container" ref={chatContainerRef}>
                    {messages.length === 0 ? (
                        <div className="welcome-message">
                            <div className="welcome-icon">👋</div>
                            <h2>Hello! I'm Jarvis</h2>
                            <p>Your personal AI assistant powered by LLaMA. Ask me anything!</p>
                        </div>
                    ) : (
                        messages.map((message, index) => (
                            <ChatMessage key={index} message={message} />
                        ))
                    )}

                    {isLoading && (
                        <div className="message assistant">
                            <div className="message-avatar">🤖</div>
                            <div className="message-content">
                                <div className="loading">
                                    <div className="loading-dot"></div>
                                    <div className="loading-dot"></div>
                                    <div className="loading-dot"></div>
                                </div>
                            </div>
                        </div>
                    )}
                </div>

                {/* Input Area */}
                <ChatInput onSendMessage={sendMessage} disabled={isLoading} />
            </div>
        </div>
    );
}

export default App;
