// Function to show the notification
function showNotification(message) {
    const notification = document.getElementById('success-notification');
    const messageElement = document.getElementById('notification-message');
    messageElement.innerText = message;
    notification.classList.remove('hidden');

    setTimeout(hideNotification, 4000);

}


// Function to hide the notification
function hideNotification() {
    const notification = document.getElementById('success-notification');
    notification.classList.add('hidden');
}

// Show the notification if a message exists
window.onload = function () {
    const messagesContainer = document.getElementById('messages');
    if (messagesContainer) {
        const message = messagesContainer.querySelector('span').innerText;
        if (message) {
            console.log("messge" + message)
            showNotification(message);
        }
    }
};