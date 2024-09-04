document.addEventListener('DOMContentLoaded', function () {
    const chatInput = document.querySelector('.chat-footer input[type="text"]');
    const chatButton = document.querySelector('.chat-footer button');
    const chatBody = document.querySelector('.chat-body');

    function addMessageToChat(message, isBot = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(isBot ? 'bot-message' : 'user-message');
        messageDiv.textContent = message;
        chatBody.appendChild(messageDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    chatButton.addEventListener('click', function () {
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            addMessageToChat(userMessage);
            chatInput.value = '';
            setTimeout(() => {
                addMessageToChat('This is a bot response.', true);
            }, 1000);
        }
    });

    chatInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            chatButton.click();
        }
    });
});
