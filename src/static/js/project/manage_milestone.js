document.addEventListener('DOMContentLoaded', () => {
    const deleteButton = document.getElementById('delete-button');
    const confirmationModal = document.getElementById('delete_confirmation');
    const confirmButton = document.getElementById('confirm-button');
    const cancelButton = document.getElementById('cancel-button');

    let deleteUrl = '';
    const projectId = JSON.parse(document.getElementById('project-id').textContent);
    deleteButton.addEventListener('click', (e) => {
        e.preventDefault();
        // Store the URL for the POST request
        deleteUrl = e.target.closest('a').href;

        confirmationModal.classList.remove('hidden');
    });

    confirmButton.addEventListener('click', () => {
        fetch(deleteUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Make sure to include CSRF token
            },
            body: JSON.stringify({}) // Include any data you need to send
        }).then(response => {
            if (response.ok) {
                window.location.href = `/project/${projectId}/milestone`; // Redirect after successful delete
            } else {
                console.error('Delete request failed');
            }
        })
            .catch(error => console.error('Error:', error));

    });

    cancelButton.addEventListener('click', () => {
        confirmationModal.classList.add('hidden');
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});




