document.getElementById('experienceForm').addEventListener('submit', function (e) {
    e.preventDefault(); 
    document.getElementById('confirmationModal').classList.remove('hidden');
});

document.getElementById('addMore').addEventListener('click', function () {
    let formData = new FormData(document.getElementById('experienceForm'));
    
    fetch("{% url 'add_experience' %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('confirmationModal').classList.add('hidden'); 
            document.getElementById('experienceForm').reset(); 
            document.getElementById('form-container').scrollIntoView({ behavior: 'smooth' });
        } else {
            alert('Hubo un error al guardar la experiencia, intenta nuevamente.');
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('submitForm').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden'); 
    document.getElementById('experienceForm').submit(); 
});

document.getElementById('closeModal').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden');
});