// Configuration
const API_URL = 'http://localhost:5000';

// DOM Elements
const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const statusDot = document.getElementById('statusDot');
const statusText = document.getElementById('statusText');

// State
let isProcessing = false;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    checkServerStatus();
    setupEventListeners();
    autoResizeTextarea();
});

// Event Listeners
function setupEventListeners() {
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    userInput.addEventListener('input', autoResizeTextarea);
}

// Auto-resize textarea
function autoResizeTextarea() {
    userInput.style.height = 'auto';
    userInput.style.height = userInput.scrollHeight + 'px';
}

// Check server status
async function checkServerStatus() {
    try {
        const response = await fetch(`${API_URL}/health`);
        const data = await response.json();
        
        if (data.status === 'running' && data.ollama_connected) {
            updateStatus('connected', 'Connected');
        } else if (data.status === 'running') {
            updateStatus('warning', 'Server running, Ollama offline');
        } else {
            updateStatus('error', 'Server offline');
        }
    } catch (error) {
        updateStatus('error', 'Server offline');
    }
}

// Update status indicator
function updateStatus(status, text) {
    statusText.textContent = text;
    statusDot.className = 'status-dot';
    
    if (status === 'connected') {
        statusDot.classList.add('connected');
    }
}

// Send message
async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message || isProcessing) return;
    
    // Clear input
    userInput.value = '';
    autoResizeTextarea();
    
    // Remove welcome message if exists
    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.remove();
    }
    
    // Add user message
    addMessage('user', message);
    
    // Show loading
    const loadingId = addLoading();
    
    // Disable input
    isProcessing = true;
    sendButton.disabled = true;
    
    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        
        const data = await response.json();
        
        // Remove loading
        removeLoading(loadingId);
        
        // Add assistant response
        if (data.success) {
            addMessage('assistant', data.response);
        } else {
            addMessage('assistant', `Error: ${data.response}`);
        }
        
    } catch (error) {
        removeLoading(loadingId);
        addMessage('assistant', 'Sorry, I could not connect to the server. Please make sure the backend is running.');
    } finally {
        isProcessing = false;
        sendButton.disabled = false;
        userInput.focus();
    }
}

// Add message to chat
function addMessage(role, content) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}`;
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = role === 'user' ? '👤' : '🤖';
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.textContent = content;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(messageContent);
    
    chatContainer.appendChild(messageDiv);
    
    // Scroll to bottom
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Add loading indicator
function addLoading() {
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message assistant';
    loadingDiv.id = 'loading-' + Date.now();
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = '🤖';
    
    const loadingContent = document.createElement('div');
    loadingContent.className = 'message-content';
    
    const loading = document.createElement('div');
    loading.className = 'loading';
    loading.innerHTML = '<div class="loading-dot"></div><div class="loading-dot"></div><div class="loading-dot"></div>';
    
    loadingContent.appendChild(loading);
    loadingDiv.appendChild(avatar);
    loadingDiv.appendChild(loadingContent);
    
    chatContainer.appendChild(loadingDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    
    return loadingDiv.id;
}

// Remove loading indicator
function removeLoading(loadingId) {
    const loadingDiv = document.getElementById(loadingId);
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

// Check status periodically
setInterval(checkServerStatus, 30000); // Every 30 seconds
