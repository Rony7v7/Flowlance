// Show success message when a file is uploaded
document.getElementById('course_image').addEventListener('change', function () {
    if (this.files.length > 0) {
        document.getElementById('uploadSuccess').classList.remove('hidden');
        setTimeout(() => {
            document.getElementById('uploadSuccess').classList.add('hidden');
        }, 3000); // Hide the message after 3 seconds
    }
});

document.getElementById('courseForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent immediate form submission
    document.getElementById('confirmationModal').classList.remove('hidden'); // Show the modal
});

document.getElementById('addMore').addEventListener('click', function () {
    // Use Fetch API to send data to the server without reloading the page
    let formData = new FormData(document.getElementById('courseForm'));
    
    fetch("{% url 'add_course' %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('confirmationModal').classList.add('hidden'); // Hide the modal
            document.getElementById('courseForm').reset(); // Reset the form
            document.getElementById('form-container').scrollIntoView({ behavior: 'smooth' }); // Scroll to the form
        } else {
            alert('There was an error saving the course, please try again.');
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('submitForm').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden'); // Hide the modal
    document.getElementById('courseForm').submit(); // Submit the form to the server
});

document.getElementById('closeModal').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden'); // Hide the modal
});