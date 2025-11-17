/**
 * Optimized Chat Interface Module
 */
export class ChatManager {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.chatInput = document.getElementById('chatInput');
        this.isProcessing = false;
        this.responses = this.initResponses();
        this.init();
    }

    init() {
        this.setupEventListeners();
    }

    initResponses() {
        return {
            experience: {
                text: "I'm currently pursuing an MSc in Data Science & AI at Bournemouth University and have a strong foundation in machine learning, data analysis, and software development. I specialize in end-to-end ML pipelines and RAG systems."
            },
            skills: {
                text: "My core skills include Python, SQL, PyTorch, TensorFlow, Docker, AWS, and various MLOps tools. I'm proficient in building scalable ML systems and deploying them to production environments."
            },
            projects: {
                text: "I've worked on various projects including AI-powered document analysis systems, real-time object detection, and stock price prediction models. Check out my projects page for detailed case studies!"
            },
            contact: {
                text: "Feel free to reach out via email at aisahabaj@gmail.com or connect with me on LinkedIn. I'm always open to discussing new opportunities and collaborations!"
            }
        };
    }

    setupEventListeners() {
        if (this.chatInput) {
            this.chatInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.handleSendMessage();
                }
            });
        }

        // Optimized quick action buttons setup
        this.setupQuickActions();
    }

    /**
     * Optimized quick action setup with delegation
     */
    setupQuickActions() {
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('quick-action-btn')) {
                const questionType = e.target.dataset.question;
                if (questionType) {
                    this.handleQuickQuestion(questionType);
                }
            }
        });
    }

    handleSendMessage() {
        if (this.isProcessing || !this.chatInput) return;

        const message = this.chatInput.value.trim();
        if (!message) return;

        this.addUserMessage(message);
        this.chatInput.value = '';
        this.processMessage(message);
    }

    handleQuickQuestion(questionType) {
        if (this.isProcessing) return;

        const response = this.responses[questionType];
        if (response) {
            this.addUserMessage(`Tell me about your ${questionType}`);
            this.addBotMessage(response.text);
        }
    }

    /**
     * Optimized message creation with template
     */
    createMessageElement(isUser, message) {
        const messageElement = document.createElement('div');

        if (isUser) {
            messageElement.className = 'message message-user';
            messageElement.innerHTML = `
                <div class="msg-bubble user-bubble">
                    <p>${message}</p>
                </div>
                <div class="msg-avatar">
                    <i class="fas fa-user"></i>
                </div>
            `;
        } else {
            messageElement.className = 'message message-bot';
            messageElement.innerHTML = `
                <div class="msg-avatar bot-avatar-icon">
                    <i class="fas fa-code"></i>
                </div>
                <div class="msg-bubble bot-bubble">
                    <p>${message}</p>
                </div>
            `;
        }

        return messageElement;
    }

    addUserMessage(message) {
        if (!this.chatMessages) return;

        const messageElement = this.createMessageElement(true, message);
        this.chatMessages.appendChild(messageElement);
        this.scrollToBottom();
    }

    addBotMessage(message) {
        if (!this.chatMessages) return;

        this.isProcessing = true;

        // Add typing indicator
        const typingElement = this.addTypingIndicator();

        setTimeout(() => {
            if (typingElement?.parentNode) {
                typingElement.remove();
            }

            const messageElement = this.createMessageElement(false, message);
            this.chatMessages.appendChild(messageElement);
            this.scrollToBottom();
            this.isProcessing = false;
        }, 1500);
    }

    addTypingIndicator() {
        if (!this.chatMessages) return;

        const typingElement = document.createElement('div');
        typingElement.className = 'message message-bot typing-indicator';
        typingElement.innerHTML = `
            <div class="msg-avatar bot-avatar-icon">
                <i class="fas fa-code"></i>
            </div>
            <div class="msg-bubble bot-bubble">
                <div class="typing-dots">
                    <span></span><span></span><span></span>
                </div>
            </div>
        `;

        this.chatMessages.appendChild(typingElement);
        this.scrollToBottom();
        return typingElement;
    }

    /**
     * Optimized message processing with keyword mapping
     */
    processMessage(message) {
        const lowerMessage = message.toLowerCase();

        // Keyword to response mapping for better maintainability
        const keywordMap = {
            experience: ['experience', 'background'],
            skills: ['skill', 'technology'],
            projects: ['project', 'work'],
            contact: ['contact', 'email', 'reach']
        };

        let responseKey = null;

        // Find matching response
        for (const [key, keywords] of Object.entries(keywordMap)) {
            if (keywords.some(keyword => lowerMessage.includes(keyword))) {
                responseKey = key;
                break;
            }
        }

        const response = responseKey
            ? this.responses[responseKey]
            : {
                text: "I'm here to help you learn more about Sahabaj's background and expertise. Try asking about his experience, skills, projects, or contact information!"
            };

        this.addBotMessage(response.text);
    }

    scrollToBottom() {
        if (this.chatMessages) {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }
    }
}

// Global functions for backward compatibility
window.askQuestion = function (questionType) {
    if (window.chatManager) {
        window.chatManager.handleQuickQuestion(questionType);
    }
};

window.sendMessage = function () {
    if (window.chatManager) {
        window.chatManager.handleSendMessage();
    }
};

window.handleKeyPress = function (event) {
    if (event.key === 'Enter' && window.chatManager) {
        window.chatManager.handleSendMessage();
    }
};
