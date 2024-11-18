document.getElementById('skillsForm').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('confirmationModal').classList.remove('hidden'); 
});

document.getElementById('addMore').addEventListener('click', function () {
    let formData = new FormData(document.getElementById('skillsForm'));
    
    fetch("{% url 'customize_profile' %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('confirmationModal').classList.add('hidden');
            document.getElementById('skillsForm').reset();
            document.getElementById('form-container').scrollIntoView({ behavior: 'smooth' }); 
        } else {
            alert('Hubo un error al guardar las habilidades, intenta nuevamente.');
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('submitForm').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden');
    document.getElementById('skillsForm').submit(); 
});

document.getElementById('closeModal').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden'); 
});