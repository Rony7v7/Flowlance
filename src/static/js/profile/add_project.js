document.getElementById('attached_files').addEventListener('change', function () {
    document.getElementById('uploadSuccess').classList.remove('hidden');
    setTimeout(() => {
        document.getElementById('uploadSuccess').classList.add('hidden');
    }, 3000);
});

document.getElementById('project_image').addEventListener('change', function () {
    document.getElementById('uploadSuccess2').classList.remove('hidden');
    setTimeout(() => {
        document.getElementById('uploadSuccess2').classList.add('hidden');
    }, 3000);
});

document.getElementById('projectForm').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('confirmationModal').classList.remove('hidden'); // Mostrar el modal
});

document.getElementById('addMore').addEventListener('click', function () {
    let formData = new FormData(document.getElementById('projectForm'));

    fetch("{% url 'add_project' %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
        .then(response => {
            if (response.ok) {
                document.getElementById('confirmationModal').classList.add('hidden');
                document.getElementById('projectForm').reset();
                document.getElementById('form-container').scrollIntoView({ behavior: 'smooth' });
            } else {
                alert('Hubo un error al guardar el proyecto, intenta nuevamente.');
            }
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('submitForm').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden');
    document.getElementById('projectForm').submit();
});

document.getElementById('closeModal').addEventListener('click', function () {
    document.getElementById('confirmationModal').classList.add('hidden');
});